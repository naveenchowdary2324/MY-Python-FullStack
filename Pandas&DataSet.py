import pandas as pp

file_path = r"C:\Users\ambat\Downloads\StressLevelDataset (1).csv" #dataset1 Path
file_path2 = r"C:\Users\ambat\Downloads\Hearing well-being Survey Report.csv" #dataset2 Path

df_Stress = pp.read_csv(file_path, encoding='latin1') #dataset1
df_wellBeingSurvey = pp.read_csv(file_path2, encoding='latin1') #dataset2

#Displayingdataset1
print("StressLevelDataset:- ")
print(df_Stress.head(),"\n")
print(df_Stress.columns,"\n")
print(df_Stress.shape,"\n")
print(df_Stress.describe,"\n")

#Displayingdataset2
print("Hearing well-being Survey Report:-")
print(df_wellBeingSurvey.head(),"\n")
print(df_wellBeingSurvey.shape,"\n")
print(df_wellBeingSurvey.columns,"\n")
print(df_wellBeingSurvey.describe(),"\n")
