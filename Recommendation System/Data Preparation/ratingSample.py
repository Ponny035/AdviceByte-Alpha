import connectDB
import random

def addRating(User_ID, Activity_ID, Interest_Score):
    connection = connectDB.mydb
    mycursor = connection.cursor()
    query = "INSERT INTO `User_Interest_Activity_List` (`User_ID`, `Activity_ID`, `Interest_Score`, `Update_At`) VALUES ('"+ str(User_ID) +"', '"+ str(Activity_ID) +"', '"+ str(Interest_Score) +"', CURRENT_TIMESTAMP)"
    mycursor.execute(query)
    connection.commit()

for i in range(1,45):
    for j in range(1,20):
        rating = random.uniform(0.0, 5.0)
        addRating(i, j, rating)
