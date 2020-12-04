import connectDB

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

def getMaxActivity(userID):
    query = "SELECT `User_ID`,`Learning_Style_ID`,`Count` FROM User_Study_History WHERE `User_ID` = "+ str(userID)
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    if myresult:
        return myresult
    else:
        return 0

def getActivity(category):
    query = "SELECT `Activity_ID` FROM `Activity` WHERE `Categories_ID` = "+ str(category)
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    if myresult:
        return myresult
    else:
        return 0

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

inputUser = 7

activitiesCount = {}

connection = connectDB.mydb
mycursor = connection.cursor()

userCluster = getUserCluster(inputUser)

cluster = getCluster(userCluster)

for i in cluster:
    activities = getMaxActivity(i[0])
    for j in activities:
        activity = j[1]
        if activity in activitiesCount:
            activitiesCount[activity].append(j[2])
        else:
            activitiesCount[activity] = []
            activitiesCount[activity].append(j[2])

maxType = 0
maxCount = 0

for key in activitiesCount.keys():
    count = sum(activitiesCount[key])
    if count > maxCount:
        maxType = key
        maxCount = count

#maxType overWrite
maxType = 1

recommendActivity = getActivity(maxType)

rank = []

for i in recommendActivity:
    rating = getRating(inputUser,i[0])
    print(i[0],rating)
    rank.append([i[0],rating])

rank.sort(reverse=True,key=sortingElement)

for i in rank:
    print(i[0])
