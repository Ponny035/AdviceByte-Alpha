import connectDB
import random


def addActivity(userID, activityID, statusID, time):
    query = "INSERT INTO `User_Activity_Status_History` (`History_ID`, `User_ID`, `Activity_ID`, `Status_ID`, `Update_At`) VALUES (NULL, '" + str(userID) + "', '" + str(activityID) + "', '" + str(statusID) + "', '" + str(time) + "')"
    mycursor.execute(query)
    connection.commit()


connection = connectDB.mydb
mycursor = connection.cursor()

for i in range(1,1000):
    userID = int(random.uniform(1, 45))
    activityID = int(random.uniform(1, 86))
    statusID = int(random.uniform(1, 4))
    month = int(random.uniform(1, 13))
    date = int(random.uniform(1, 29))
    time = "2020-"+str(month)+"-"+str(date)+" 07:22:50"
    print(userID,activityID,statusID,time)
    addActivity(userID,activityID,statusID,time)
    print("round",i)
