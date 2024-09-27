import pandas as pd 
str_file_path = "StudentPerformanceFactors.csv"

df_file = pd.read_csv(str_file_path)

#df_file["Teacher_Quality"] = df_file["Teacher_Quality"].convert_dtypes(convert_string=True)
df_file["Teacher_Quality"].replace("Low" , 1, inplace=True)
df_file["Teacher_Quality"].replace("Medium" , 2, inplace=True)
df_file["Teacher_Quality"].replace("High" , 3, inplace=True)
print (df_file["Teacher_Quality"])

#low = 1
#medium = 2 
#height = 3

print(df_file.describe())

#print(df_file.describe())
#print (df_file.pivot_table(values=["Hours_Studied"], columns= "Gender", index= ["Exam_Score"], fill_value=0, aggfunc="mean", )) 
