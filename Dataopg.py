import pandas as pd
import numpy as np
import matplotlib .pyplot as plt


df1 = pd.read_table("u.user.txt", sep= '|')
#Print dataframe
print("Original Dataframe")
print (df1)

#Grupper occupation og age og find gennemsnitsalderen
grouped_df = df1.groupby('occupation')['age'].mean().reset_index()
average_age = df1.groupby('gender')['age'].mean()
gender_counts = df1['gender'].value_counts()

print("\nGrouped DataFrame (Average Age by Occupation):")
print (grouped_df)
print("\nAverage Age by Gender:")
print(average_age)
print("\nGender Counts:")
print(gender_counts)

#Plot average age by occupation
plt.figure(figsize=(10,5))
plt.xticks(rotation=45, ha = 'right')
plt.tight_layout()
plt.bar(grouped_df['occupation'], grouped_df['age'], color='skyblue')
plt.title('Average age by occupation')
plt.xlabel('Occupation')
plt.ylabel('Age')
plt.show()

#Plot Average age by gender
plt.figure(figsize=(6,4))
plt.bar(average_age['average age'], average_age['gender'], color ='red')
plt.title('Average age by occupation')
plt.xlabel('average age')
plt.ylabel('age')
plt.show()

#Plot gender counts
plt.figure(figsize=(10,5))
plt.bar(gender_counts['men'], gender_counts['women'], color = 'pink')
plt.title('gender count')
plt.xlabel('Gender')
plt.ylabel('Amount')
plt.show

#Kig datasættet igennem
# Kan man vurdere kvaliteten
# Lave en præsentation
