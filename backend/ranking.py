import connectDB
import sys
import json

def getInformation(userId):
    query = "SELECT `User_Name` FROM `User_Information` WHERE `User_ID` = "+ str(userId)
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult[0][0]

def getActivityCount():
    query = "SELECT `User_ID`, COUNT(`User_ID`) AS count FROM `User_Activity_Status_History` WHERE (CURRENT_DATE - DATE(`Update_At`)) < 30 AND `Status_ID` = 3  GROUP BY `User_ID` ORDER BY `count`  DESC,`User_ID`"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult

def findRank(userId, listActivity):
    list = listActivity
    rank = 0
    for i in list:
        rank = rank + 1
        if userId == str(i[0]):
            return rank
    return 0


connection = connectDB.mydb
mycursor = connection.cursor()
userId = sys.argv[1]

listActivity = getActivityCount()
rank = findRank(userId, listActivity)

listRankName = []
listRankPosition = []

if rank<4:
    for i in range(5):
        listRankName.append(getInformation(listActivity[i][0]))
        listRankPosition.append((i+1))
else:
    for i in range(4):
        listRankName.append(getInformation(listActivity[i][0]))
        listRankPosition.append((i+1))
    listRankName.append(getInformation(userId))
    listRankPosition.append(rank)

print(json.dumps(listRankName))
print(json.dumps(listRankPosition))
