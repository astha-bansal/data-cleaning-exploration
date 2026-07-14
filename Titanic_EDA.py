import pandas as pd
import numpy as np

df=pd.read_csv("Titanic-Dataset.csv")
print("Rows:", df.shape[0], "Columns:",df.shape[1])

#Inspect the Data:
#first 5 rows
print(df.head())
#COlumn names and data types
print(df.dtypes)
#Quick statistical summary of ALL numeric columns
print(df.describe())

#Finding Missing Values
#Count missing value in each column
print(df.isnull().sum())
#Show as percenatge
missing_pct=(df.isnull().sum()/len(df))*100;
print(missing_pct.round(2))

# Handle Missing Values
# Strategy A: Fill missing Age with the MEDIAN age
# (Median is better than mean when there are outliers)
df['Age']=df['Age'].fillna(df['Age'].median())
# Strategy B: Fill missing Embarked with the most common value (mode)
df['Embarked']=df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
# Strategy C: Drop the Cabin column (too many missing values)
df=df.drop(columns=['Cabin'])
# Verify - should now show 0 for Age and Embarked
print(df.isnull().sum())

#Remove duplicates
# Check for duplicate rows
print('Duplicates before:', df.duplicated().sum())
# Remove duplicates
df=df.drop_duplicates()
print('Duplicates after:', df.duplicated().sum())
print('Final dataset shape:', df.shape)

# Exploratory Analysis – Ask Questions with Code
# Q1: How many passengers survived?
print('Survived:', df['Survived'].value_counts())
print('Survival Rate:', df['Survived'].mean() * 100, '%')
# Q2: What was the average age by passenger class?
print(df.groupby('Pclass')['Age'].mean().round(1))
# Q3: Did women survive more than men?
print(df.groupby('Sex')['Survived'].mean() * 100)
# Q4: Correlation between Fare paid and survival?
print(df[['Fare','Survived','Age']].corr().round(2))

# Create Computed Columns
# Create a 'FamilySize' column (siblings + parents + self)
df['FamilySize']=df['SibSp']+df['Parch']+1;
# Create 'IsAlone' column - 1 if travelling alone, 0 otherwise
df['IsAlone']=(df['FamilySize']==1).astype(int)
# Create Age groups
df['AgeGroup'] = pd.cut(df['Age'],
bins=[0, 12, 18, 35, 60, 100],
labels=['Child','Teen','Young Adult','Adult','Senior'])
print(df[['Age','AgeGroup','FamilySize','IsAlone']].head(8))

# Save the Cleaned Dataset
# Save cleaned dataset to a new CSV file
df.to_csv('titanic_cleaned.csv', index=False)
print('Cleaned dataset saved! Rows:', len(df))
# Verify it saved correctly
df_check = pd.read_csv('titanic_cleaned.csv')
print('Loaded back successfully:', df_check.shape)