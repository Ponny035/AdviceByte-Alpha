import connectDB
import sys

def getUserCluster(userID):
    query = "SELECT `Study_Cluster_ID` FROM `User_Information`  WHERE `User_ID` = "+ str(userID)
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult[0][0]

def getCluster(clusterID):
    query = "SELECT `User_ID` FROM `User_Information`  WHERE `Study_Cluster_ID` = "+ str(clusterID)
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult

def getMaxLearningStyle(userID):
    query = "SELECT `User_ID`,`Learning_Style_ID`,`Count` FROM User_Study_History WHERE `User_ID` = "+ str(userID)+ " ORDER BY `Count`  DESC"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    if myresult:
        return myresult
    else:
        return 0

def getActivity(learningStyle):
    query = "SELECT `Activity_ID` FROM `Activity` WHERE `Categories_ID` = " + str(learningStyle)
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    if myresult:
        return myresult
    else:
        return 0

def getActivityBySkills(learningStyle, skills):
    for style in learningStyle:
        query = "SELECT c1.`Categories_ID` FROM `Categories` AS c1,`Categories_Skills` AS c2,`Categories_Style`AS c3 WHERE c1.`Categories_ID` = c2.`Categories_ID` AND c2.`Categories_ID` = c3.`Categories_ID` AND c1.`Categories_ID` = c3.`Categories_ID` AND `Skill_ID` = " + str(skill) + " AND `Learning_Style_ID` = " + str(style[0])
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        if myresult:
            return getActivity(myresult[0][0])
    return getActivity(learningStyle[0][0])

def getRating(userID, activityID):
    query = "SELECT `Interest_Score` FROM `User_Interest_Activity_List` WHERE `User_ID` = "+ str(userID) +" AND `Activity_ID` = "+ str(activityID)
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    if myresult:
        return myresult[0][0]
    else:
        return 2.5

def sortingElement(e):
  return e[1]

# #inputUser overWrite
# inputUser = 7
inputUser = sys.argv[1]

DicLearningStyle = {}

connection = connectDB.mydb
mycursor = connection.cursor()

userCluster = getUserCluster(inputUser)

cluster = getCluster(userCluster)

for i in cluster:
    learningStyle = getMaxLearningStyle(i[0])
    for j in learningStyle:
        style = j[1]
        if style in DicLearningStyle:
            DicLearningStyle[style].append(j[2])
        else:
            DicLearningStyle[style] = []
            DicLearningStyle[style].append(j[2])

learningStyleCount = []

for key in DicLearningStyle.keys():
    count = sum(DicLearningStyle[key])
    learningStyleCount.append([key,count])

learningStyleCount.sort(reverse=True,key=sortingElement)
# #maxType overWrite
# maxType = 1
maxType = learningStyleCount[0][0]

if(len(sys.argv) != 3):
    recommendActivity = getActivity(maxType)
else:
    skill = sys.argv[2]
    recommendActivity = getActivityBySkills(learningStyleCount,skill)

rank = []

for i in recommendActivity:
    rating = getRating(inputUser,i[0])
    rank.append([i[0],rating])

rank.sort(reverse=True,key=sortingElement)

for i in rank:
    print(i[0])
