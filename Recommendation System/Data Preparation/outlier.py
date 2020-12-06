import pandas as pd
import numpy as np
import unicodecsv
import sys


data = pd.read_csv('../Data/cleaning/mappedData.csv', encoding='utf-8')

# Computing IQR
Q1 = data['Total'].quantile(0.25)
Q3 = data['Total'].quantile(0.75)
IQR = Q3 - Q1

filtered = data.query('(@Q1 - 1.5 * @IQR) <= Total <= (@Q3 + 1.5 * @IQR)')

filtered_list = filtered.values.tolist()

with open('../Data/cleaning/cleanedData.csv', 'wb') as f:
    f.write(u'\ufeff'.encode('utf8'))
    writer = unicodecsv.writer(f,encoding='utf8')
    writer.writerow(["Time", "Status", "Type", "Algorithm","DataStructure","Programming","Mathematic",
                    "Language","Communication", "ProblemSolving","SelfMotivation","Total",
                    "StudyHardSkill","TestHardSkill","StudySoftSkill","TestSoftSkill"])

    for row in filtered_list:
        writer.writerow(row)
