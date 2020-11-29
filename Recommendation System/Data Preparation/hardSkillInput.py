import connectDB
import pandas as pd
import numpy as np
import unicodecsv

connection = connectDB.mydb

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

def LearningStyle(category):
    query = "SELECT Learning_Style_ID FROM Categories_Style WHERE Categories_ID = " + str(category)
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    for x in myresult:
      style = x[0]
      query = "SELECT `Count` FROM `Study_Cluster` WHERE `Cluster_MBTI_ID` = "+ str(type) +" AND `Cluster_Learning_Style_ID` = "+ str(style)
      mycursor.execute(query)
      result = mycursor.fetchall()
      count = result[0][0]+1
      query = "UPDATE Study_Cluster SET Count = "+str(count)+", Update_At = CURRENT_TIMESTAMP, Admin_ID = 3 WHERE Cluster_MBTI_ID= "+ str(type) +" AND `Cluster_Learning_Style_ID` = "+ str(style)
      mycursor.execute(query)
      connection.commit()


mycursor = connection.cursor()

data = pd.read_csv("../Data/cleaning/hardSkillStudyActivities.csv")

data_list = data.values.tolist()

with open("../Data/cleaning/hardSkillLeftOverData.csv", 'wb') as f:
    f.write(u'\ufeff'.encode('utf8'))
    writer = unicodecsv.writer(f,encoding='utf8')
    writer.writerow(["Type", "Activity"])
    for row in data_list:
        if(row[0] is not 0):
            type = row[0]
            activities = row[1].split("/")
            for activity in activities:
                category = CategoriesFinder(activity)
                if(category is not 0):
                    LearningStyle(category)
                else:
                    writer.writerow([type,activity])
