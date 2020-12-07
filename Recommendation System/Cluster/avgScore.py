import connectDB

def getAVGScore():
    query = "SELECT AVG(`Algorithm_Score`), AVG(`Data_Structure_Score`), AVG(`Programming_Score`), AVG(`Mathematic_Score`), AVG(`Language_Score`), AVG(`Communication_Score`), AVG(`Problem_Solving_Score`), AVG(`Self_Motivation_Score`) FROM `User_Information` WHERE `User_ID` != 0"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult[0]

def updateSystemAVG(AlgorithmAVG, DataStructureAVG, ProgrammingAVG, MathematicAVG, LanguageAVG, CommunicationAVG, ProblemSolvingAVG, SelfMotivationAVG):
    query = "UPDATE `User_Information` SET `Algorithm_Score` = '" + str(AlgorithmAVG) + "', `Data_Structure_Score` = '" + str(DataStructureAVG) + "', `Programming_Score` = '" + str(ProgrammingAVG) + "', `Mathematic_Score` = '" + str(MathematicAVG) + "', `Language_Score` = '" + str(LanguageAVG) + "', `Communication_Score` = '" + str(CommunicationAVG) + "', `Problem_Solving_Score` = '" + str(ProblemSolvingAVG) + "', `Self_Motivation_Score` = '" + str(SelfMotivationAVG) + "', `Update_At` = CURRENT_TIMESTAMP WHERE `User_Information`.`User_ID` = 0"
    mycursor.execute(query)
    connection.commit()


connection = connectDB.mydb
mycursor = connection.cursor()

AVG = getAVGScore()
print(AVG)
updateSystemAVG(int(AVG[0]), int(AVG[1]), int(AVG[2]), int(AVG[3]), int(AVG[4]), int(AVG[5]), int(AVG[6]), int(AVG[7]))
