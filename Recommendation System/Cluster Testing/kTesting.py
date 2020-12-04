import connectDB
from pandas import DataFrame
import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial import distance
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import sys

connection = connectDB.mydb

def getUserData():
    query = "SELECT `User_ID`,`MBTI_ID`,`Algorithm_Score`,`Data_Structure_Score`,`Programming_Score`,`Mathematic_Score`,`Language_Score`,`Communication_Score`,`Problem_Solving_Score`,`Self_Motivation_Score` FROM `User_Information`"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult

def updateUserCluster(userID, cluster):
    query = "UPDATE `User_Information` SET `Study_Cluster_ID`="+str(cluster)+",`Update_At`= CURRENT_TIMESTAMP WHERE `User_ID` = " + str(userID)
    mycursor.execute(query)
    connection.commit()
    print("UPDATED User Cluster")

def updateClusterCenter(clusterID, MBTICenter, AlgorithmCenter, DataStructureCenter, ProgrammingCenter, MathematicCenter, LanguageCenter, CommunicationCenter, ProblemSolvingCenter, SelfMotivationCenter):
    query = "UPDATE `Study_Cluster` SET `MBTI_Center`="+str(MBTICenter)+",`Algorithm_Score_Center`="+str(AlgorithmCenter)+",`Data_Structure_Score_Center`="+str(DataStructureCenter)+",`Programming_Score_Center`="+str(ProgrammingCenter)+",`Mathematic_Score_Center`="+str(MathematicCenter)
    query = query +",`Language_Score_Center`="+str(LanguageCenter)+",`Communication_Score_Center`="+str(CommunicationCenter)+",`Problem_Solving_Score_Center`="+str(ProblemSolvingCenter)+",`Self_Motivation_Score_Center`="+str(SelfMotivationCenter)+",`Update_At`=CURRENT_TIMESTAMP,`Admin_ID`=3 WHERE `Study_Cluster_ID` = " + str(clusterID)
    mycursor.execute(query)
    connection.commit()
    print("UPDATED centroid")


mycursor = connection.cursor()

query = getUserData()

data = DataFrame (query,columns=['User_ID','MBTI_ID','Algorithm_Score','Data_Structure_Score','Programming_Score','Mathematic_Score','Language_Score','Communication_Score','Problem_Solving_Score','Self_Motivation_Score'])
train = data.drop(columns=['User_ID'])

kmeans = KMeans(n_clusters=7)
kmeans.fit(train)
centroids  = kmeans.cluster_centers_
clusters = kmeans.labels_

internalError = []
externalError = []
dunnIndex = []

for i in range (1,len(train)+1):
    print("Number of cluster",i)
    sumInter = 0
    sumExter = 0
    sumDunn = 0
    for j in range(10):
        kmeans = KMeans(n_clusters=i)
        kmeans.fit(train)
        centroids  = kmeans.cluster_centers_
        cluster = kmeans.labels_
        minExter = (2**63)-1
        maxInter = -1*(2**63)
        for k in range(len(data)):
            value = train.loc[[k]]
            centroid = centroids[cluster[k]]
            dist = distance.euclidean(value, centroid)
            sumInter += dist
            if maxInter < dist:
                maxInter = dist
        for k in range(len(centroids)):
            for l in range(k+1,len(centroids)):
                dist = distance.euclidean(centroids[k], centroids[l])
                sumExter += dist
                if minExter > dist:
                    minExter = dist
        if maxInter != 0:
            sumDunn += minExter/maxInter
        else:
            sumDunn += (2**63)-1

    sumExter = sumExter/10
    sumInter = sumInter/10
    sumDunn = sumDunn/10
    print("Avg Internal Error = ",sumInter)
    print("Avg External Error = ",sumExter)
    print("Avg Dunn Index = ",sumDunn)
    internalError.append(sumInter)
    externalError.append(sumExter)
    dunnIndex.append(sumDunn)

print("Internal Error")
for i in internalError:
    print(i)

print("External Error")
for i in externalError:
    print(i)

print("Dunn Index")
for i in dunnIndex:
    print(i)
