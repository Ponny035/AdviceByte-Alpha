import connectDB
import random

def getActivityCount(userID):
    query = "SELECT COUNT(`User_ID`) AS count FROM `User_Activity_Status_History` WHERE (CURRENT_DATE - DATE(`Update_At`)) < 30 AND `Status_ID` = 3 AND `User_ID` = " + str(userID) + " GROUP BY `User_ID`"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult[0][0]

def getActivityList(userID):
    query = "SELECT `Activity_ID` AS count FROM `User_Activity_Status_History` WHERE (CURRENT_DATE - DATE(`Update_At`)) < 30 AND `Status_ID` = 3 AND `User_ID` = " + str(userID)
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult

def getSkillList(activityID):
    query = "SELECT `Skill_ID` FROM `Categories_Skills` WHERE `Categories_ID` = (SELECT `Categories_ID` FROM `Activity` WHERE `Activity_ID` = " + str(activityID) + ")"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult

def getTopLearningStyle(userID):
    query = "SELECT `Learning_Style_ID`,`Count` FROM User_Study_History WHERE `User_ID` = "+ str(userID)+ " ORDER BY `Count`  DESC"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult[0][0]

def sortingElement(e):
  return e[1]

def getTotalLeaf(activityCount):
    if activityCount < 7:
        return 2
    elif activityCount < 12:
        return 8
    else:
        return 18

connection = connectDB.mydb
mycursor = connection.cursor()

userID = 3

totalLeaf = getTotalLeaf(getActivityCount(userID))

activityList = getActivityList(userID)

DicLearningStyle = {}

for activity in activityList:
    activity = activity[0]
    learningStyleList = getSkillList(activity)
    for learningStyle in learningStyleList:
        style = learningStyle[0]
        if style in DicLearningStyle:
            DicLearningStyle[style].append(1)
        else:
            DicLearningStyle[style] = []
            DicLearningStyle[style].append(1)

learningStyleCount = []

for key in DicLearningStyle.keys():
    count = sum(DicLearningStyle[key])
    learningStyleCount.append([key,count])

learningStyleCount.sort(reverse=True,key=sortingElement)

firstSkill = learningStyleCount[0][1]
secondSkill = learningStyleCount[1][1]
thirdSkill = learningStyleCount[2][1]

totalUserSkillCount = firstSkill+secondSkill+thirdSkill

proportionOne = round((firstSkill/totalUserSkillCount) * totalLeaf)
proportionTwo = round((secondSkill/totalUserSkillCount) * totalLeaf)
proportionThree = totalLeaf - proportionOne - proportionTwo

for i in range(totalLeaf):
    leafColor =[]
    for j in range(proportionOne):
        leafColor.append(learningStyleCount[0][1])
    for j in range(proportionTwo):
        leafColor.append(learningStyleCount[1][1])
    for j in range(proportionThree):
        leafColor.append(learningStyleCount[2][1])

random.shuffle(leafColor)
print(leafColor)
