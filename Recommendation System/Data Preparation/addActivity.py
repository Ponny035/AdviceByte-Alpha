import connectDB
import pandas as pd
import numpy as np

Categories = {
    "Coding":1,
    "Hackathon":2,
    "Project":3,
    "Working":4,
    "Contest":5,
    "Offline Study":6,
    "Seminar":7,
    "Workshop":8,
    "Online Study":9,
    "Self Study":10,
    "Reading Writing":11,
    "Community Study":12,
    "Developing":13,
    "Public Speaking":14,
    "Movie":15,
    "Gaming":16,
    "Teaching":17
    }

def CategoriesFinder(activity):
    category = 0
    if activity in Categories:
        category = Categories[activity]
    else :
        activity = activity.strip()
        query = "SELECT Categories_ID FROM Categories_Alternative_Name WHERE Activity_Alternative_Name = \"" + activity+ "\""
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        for x in myresult:
            category = x[0]
    if(category == 0):
        print(activity)
    return category

def addActivity(Activity_Name, Categories_ID):
    connection = connectDB.mydb
    mycursor = connection.cursor()
    query = "INSERT INTO `Activity` (`Activity_Name`, `Activity_Description`, `Categories_ID`, `Create_At`, `Update_At`, `Admin_ID`) VALUES ('" + str(Activity_Name) + "', '-', '" + str(Categories_ID) + "', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, '3')"
    mycursor.execute(query)
    connection.commit()


data = pd.read_csv("../Data/ActivityData.csv", encoding='utf-8')

data_list = data.values.tolist()

for row in data_list:
    addActivity(row[1],CategoriesFinder(row[0]))
