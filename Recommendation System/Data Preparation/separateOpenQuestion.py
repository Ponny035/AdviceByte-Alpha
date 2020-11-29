import pandas as pd
import numpy as np
import unicodecsv

def mapSkillActivities (dicOfActivity):
    mappedActivities = {}

    for type in dicOfActivity.keys():
        listOfActivities = dicOfActivity[type]
        for details in listOfActivities:
            detail = details.strip()
            detail = detail.replace('"', '')
            activities = detail.split(",")
            for activity in activities:
                activity = activity.strip()
                if type in mappedActivities:
                    mappedActivities[type].append(activity)
                else:
                    mappedActivities[type] = []
                    mappedActivities[type].append(activity)
    return mappedActivities

def writeToCSV (CSVName, skill, dicOfActivity):
    filePath = "../Data/cleaning/"+CSVName
    with open(filePath+".csv", 'wb') as f:
        f.write(u'\ufeff'.encode('utf8'))
        writer = unicodecsv.writer(f,encoding='utf8')
        writer.writerow(["Type", skill])
        for type in dicOfActivity.keys():
            activities = dicOfActivity[type]
            for activity in activities:
                writer.writerow([type,activity])

#Include Outlier because who best or poor also have their own way to learn
data = pd.read_csv("../Data/mappedData.csv")

data_list = data.values.tolist()

dicStudyHardSkill = {}
dicTestHardSkill = {}
dicStudySoftSkill = {}
dicTestSoftSkill = {}


for row in data_list:
    type = row[2]
    if type in dicStudyHardSkill:
        dicStudyHardSkill[type].append(row[12])
        dicTestHardSkill[type].append(row[13])
        dicStudySoftSkill[type].append(row[14])
        dicTestSoftSkill[type].append(row[14])
    else:
        dicStudyHardSkill[type] = []
        dicTestHardSkill[type] = []
        dicStudySoftSkill[type] = []
        dicTestSoftSkill[type] = []
        dicStudyHardSkill[type].append(row[12])
        dicTestHardSkill[type].append(row[13])
        dicStudySoftSkill[type].append(row[14])
        dicTestSoftSkill[type].append(row[14])

writeToCSV("hardSkillStudyActivities", "StudyActivities", mapSkillActivities (dicStudyHardSkill))

writeToCSV("hardSkillTestActivities", "TestActivities", mapSkillActivities (dicTestHardSkill))

writeToCSV("softSkillStudyActivities", "StudyActivities", mapSkillActivities (dicStudySoftSkill))

writeToCSV("softSkillTestActivities", "TestActivities", mapSkillActivities (dicTestSoftSkill))
