import connectDB
import pandas as pd
import numpy as np

def addUser(User_Name, Password, First_Name, Last_Name, E_Mail, MBTI_ID, Study_Cluster_ID,
            Algorithm_Score, Data_Structure_Score, Programming_Score, Mathematic_Score,
            Language_Score, Problem_Solving_Score, Communication_Score, Self_Motivation_Score):
    connection = connectDB.mydb
    mycursor = connection.cursor()
    query = "INSERT INTO `User_Information` (`User_ID`, `User_Name`, `Password`, `First_Name`, `Last_Name`, `E_Mail`, `MBTI_ID`, `Study_Cluster_ID`,"
    query = query + "`Algorithm_Score`, `Data_Structure_Score`, `Programming_Score`, `Mathematic_Score`, `Language_Score`, `Communication_Score`,"
    query = query + "`Problem_Solving_Score`, `Self_Motivation_Score`, `Create_At`, `Update_At`)"
    query = query + "VALUES (NULL, '" + User_Name + "', '" + Password + "', '" + First_Name + "', '" + Last_Name + "', '" + E_Mail + "', '" + MBTI_ID + "', '" + Study_Cluster_ID + "', '"
    query = query + Algorithm_Score + "', '" + Data_Structure_Score + "', '" + Programming_Score + "', '" + Mathematic_Score + "', '"
    query = query + Language_Score + "', '" + Problem_Solving_Score + "', '" + Communication_Score + "', '" + Self_Motivation_Score + "', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"
    mycursor.execute(query)
    connection.commit()


data = pd.read_csv("../Data/cleaning/mappedData.csv", encoding='utf-8')

data_list = data.values.tolist()

i = 0
for row in data_list:
    i += 1
    addUser("user"+str(i), "-", "Test", str(i), "Test" + str(i) + "@advicebyte.com", str(row[2]), "0", str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]), str(row[9]),  str(row[10]))
