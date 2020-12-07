import connectDB
from pandas import DataFrame
import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial import distance

def getUserData():
    query = "SELECT `User_ID`,`MBTI_ID`,`Learning_Style_ID`,`Algorithm_Score`,`Data_Structure_Score`,`Programming_Score`,`Mathematic_Score`,`Language_Score`,`Communication_Score`,`Problem_Solving_Score`,`Self_Motivation_Score` FROM `User_Information` WHERE `User_ID` != 0"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult

def updateUserCluster(userID, cluster):
    query = "UPDATE `User_Information` SET `Study_Cluster_ID`="+str(cluster)+",`Update_At`= CURRENT_TIMESTAMP WHERE `User_ID` = " + str(userID)
    mycursor.execute(query)
    connection.commit()
    print("UPDATED User Cluster")

def updateClusterCenter(clusterID, MBTICenter, LearningStyleCenter, AlgorithmCenter, DataStructureCenter, ProgrammingCenter, MathematicCenter, LanguageCenter, CommunicationCenter, ProblemSolvingCenter, SelfMotivationCenter):
    query = "UPDATE `Study_Cluster` SET `MBTI_Center`="+str(MBTICenter)+",`Learning_Style_Center`="+str(LearningStyleCenter)+",`Algorithm_Score_Center`="+str(AlgorithmCenter)+",`Data_Structure_Score_Center`="+str(DataStructureCenter)+",`Programming_Score_Center`="+str(ProgrammingCenter)+",`Mathematic_Score_Center`="+str(MathematicCenter)
    query = query +",`Language_Score_Center`="+str(LanguageCenter)+",`Communication_Score_Center`="+str(CommunicationCenter)+",`Problem_Solving_Score_Center`="+str(ProblemSolvingCenter)+",`Self_Motivation_Score_Center`="+str(SelfMotivationCenter)+",`Update_At`=CURRENT_TIMESTAMP,`Admin_ID`=3 WHERE `Study_Cluster_ID` = " + str(clusterID)
    mycursor.execute(query)
    connection.commit()
    print("UPDATED centroid")

connection = connectDB.mydb
mycursor = connection.cursor()

query = getUserData()

data = DataFrame (query,columns=['User_ID','MBTI_ID','Learning_Style_ID','Algorithm_Score','Data_Structure_Score','Programming_Score','Mathematic_Score','Language_Score','Communication_Score','Problem_Solving_Score','Self_Motivation_Score'])
train = data.drop(columns=['User_ID'])

kmeans = KMeans(n_clusters=5)
kmeans.fit(train)
centroids  = kmeans.cluster_centers_
clusters = kmeans.labels_

counter = 0
for centroid in centroids:
    updateClusterCenter(counter,centroid[0],centroid[1],centroid[2],centroid[3],centroid[4],centroid[5],centroid[6],centroid[7],centroid[8],centroid[9])
    counter += 1

for i in range(len(data)):
    print(i)
    cluster = clusters[i]
    userID = data['User_ID'][i]
    updateUserCluster(userID, cluster)
