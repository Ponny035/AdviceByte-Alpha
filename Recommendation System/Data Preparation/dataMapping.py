import pandas as pd
import numpy as np
import unicodecsv
import sys

def mapTime(arg):
    switcher = {
        "Less than 1 year.": 0,
        "1-5 years.": 1,
        "5-10 years.": 2,
        "More than 10 years.": 3,
        "น้อยกว่า 1 ปี": 0,
        "1-5 ปี": 1,
        "6-10 ปี": 2,
        "มากกว่า 10 ปี": 3
    }
    return switcher.get(arg, -1)

def mapStatus(arg):
    switcher = {
        "": 0,
        "กำลังศึกษาอยู่ในสาขาวิทยาการคอมพิวเตอร์ หรือ สาขาที่เกี่ยวข้องกับคอมพิวเตอร์": 1,
        "กำลังทำงานเป็นนักพัฒนา หรือ ทำงานเกี่ยวกับคอมพิวเตอร์": 2,
        "อาจารย์ผู้สอนในสาขาวิทยาการคอมพิวเตอร์หรือ สาขาที่เกี่ยวข้อง": 3,
        "Studying in Computer Science student or computer related field.": 1,
        "Working as Developer or in computer related field.": 2,
        "Instructors in computer science or related fields.": 3
    }
    return switcher.get(arg, 4)

def mapType(arg):
    switcher = {
        "I don't know": 0,
        "ไม่ทราบ": 0,
        "INTJ": 1,
        "INTP": 2,
        "ENTJ": 3,
        "ENTP": 4,
        "INFJ": 5,
        "INFP": 6,
        "ENFJ": 7,
        "ENFP": 8,
        "ISTJ": 9,
        "ISFJ": 10,
        "ESTJ": 11,
        "ESFJ": 12,
        "ISTP": 13,
        "ISFP": 14,
        "ESTP": 15,
        "ESFP": 16
    }
    return switcher.get(arg, -1)

fileName = sys.argv[1]
print(fileName)

filePath = "../Data/" + fileName

data = pd.read_csv(filePath, encoding='utf-8')

data_list = data.values.tolist()

already_seen = {}

duplicates = 0


with open('../Data/cleaning/mappedData.csv', 'wb') as f:
    f.write(u'\ufeff'.encode('utf8'))
    writer = unicodecsv.writer(f,encoding='utf8')
    writer.writerow(["Time", "Status", "Type", "Algorithm","DataStructure","Programming","Mathematic",
                    "Language","Communication", "ProblemSolving","SelfMotivation","Total",
                    "StudyHardSkill","TestHardSkill","StudySoftSkill","TestSoftSkill"])

    for row in data_list:
        rowShift = 0

        if row[2] == "English":
            rowShift = 47

        time = mapTime(row[rowShift+3])
        job = mapStatus(row[rowShift+4])
        type = mapType(row[rowShift+5])
        algorithm = (int)(row[rowShift+6] + row[rowShift+7] + row[rowShift+8] + row[rowShift+9] + row[rowShift+10]) * 5
        dataStructure = (int)(row[rowShift+11] + row[rowShift+12] + row[rowShift+13] + row[rowShift+14] + row[rowShift+15]) * 5
        programming = (int)(row[rowShift+16] + row[rowShift+17] + row[rowShift+18] + row[rowShift+19] + row[rowShift+20]) * 5
        mathematic = (int)(row[rowShift+21] + row[rowShift+22] + row[rowShift+23] + row[rowShift+24] + row[rowShift+25]) * 5

        studyHardSkill = row[rowShift+26]
        testHardSkill = row[rowShift+27]

        language = (int)(row[rowShift+28] + row[rowShift+29] + row[rowShift+30] + row[rowShift+31] + row[rowShift+32]) * 5
        communication = (int)(row[rowShift+33] + row[rowShift+34] + row[rowShift+35] + row[rowShift+36] + row[rowShift+37]) * 5
        ProblemSolving = (int)(row[rowShift+38] + row[rowShift+39] + row[rowShift+40] + row[rowShift+41] + row[rowShift+42]) * 5
        selfMotivation = (int)(row[rowShift+43] + row[rowShift+44] + row[rowShift+45] + row[rowShift+46] + (4-row[rowShift+47])) * 5

        studySoftSkill = row[rowShift+48]
        testSoftSkill = row[rowShift+49]

        total = algorithm + dataStructure + programming + mathematic + language + communication + ProblemSolving +selfMotivation

        line = [time, job, type, algorithm, dataStructure, programming, mathematic,language, communication, ProblemSolving, selfMotivation, total, studyHardSkill, testHardSkill, studySoftSkill, testSoftSkill]

        keys = str(time)+str(job)+str(type)+str(algorithm)+str(dataStructure)+str(programming)+str(mathematic)+str(language)+str(communication)+str(ProblemSolving)+str(selfMotivation)+studyHardSkill+testHardSkill+studySoftSkill+testSoftSkill

        if keys not in already_seen:
            already_seen[keys] = []
            already_seen[keys].append(1)
            writer.writerow(line)
        else:
            duplicates += 1

    print("Found " + str(duplicates) + " duplicated values")
