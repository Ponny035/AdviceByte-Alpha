import connectDB
import random
import sys

skill = {
    1:"Algorithm",
    2:"Data Structure",
    3:"Coding",
    4:"Mathematic",
    5:"Language",
    6:"Communication",
    7:"Problem Solving",
    8:"Self Motivation"
    }

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

def mapColor(skill):
    switcher = {
        1: ["#4b596b","#8a94a3"],
        2: ["#a695c1","#63628c"],
        3: ["#be231f","#e14541"],
        4: ["#f68711","#f76e10"],
        5: ["#89c9b9","#0c6a58"],
        6: ["#7dac28","#8fc430"],
        7: ["#d7c388","#dab073"],
        8: ["#f68dab","#f57c95"],
    }
    return switcher.get(skill, -1)

connection = connectDB.mydb
mycursor = connection.cursor()

# #inputUser overWrite
# userID = 7
userID = sys.argv[1]

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
        leafColor.append(learningStyleCount[0][0])
    for j in range(proportionTwo):
        leafColor.append(learningStyleCount[1][0])
    for j in range(proportionThree):
        leafColor.append(learningStyleCount[2][0])

random.shuffle(leafColor)

skillLabel = {}

skillLabel[skill[learningStyleCount[0][0]]] = mapColor(learningStyleCount[0][0])[1]
skillLabel[skill[learningStyleCount[1][0]]] = mapColor(learningStyleCount[1][0])[1]
skillLabel[skill[learningStyleCount[2][0]]] = mapColor(learningStyleCount[2][0])[1]

skillColor = []
skillPos = []
offset = 13

for leaf in leafColor:
    color = mapColor(leaf)
    skillColor.append(color[0])
    skillPos.append(offset)
    skillColor.append(color[1])
    skillPos.append(offset+1)
    offset = offset + 2

print(skillLabel)
print(skillColor)
print(skillPos)
