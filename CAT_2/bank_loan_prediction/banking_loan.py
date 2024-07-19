import pandas as pd
from IPython.display import display
import numpy as np



data_df = pd.read_csv("../../data_sets/train_loan_data.csv")
print("First 10 lines of the data file")
print(data_df.head())
print("\n")
print("The column names of the file")
print(data_df.info())
print("\n")
print("The rows and columns of the data frame are:")
print(data_df.shape)
print("\n")


#checking for missing values in the entire dataset
print("checking for missing values in the entire data set")
print(data_df.isna().sum())
print("\n")
#print all the rows with the missing values
print("all the rows with the missing values")
filtered_data = data_df.isna().any(axis=1)
empty_rows_df = data_df[filtered_data]  
print(empty_rows_df) #134 rows with missing values
print("\n")

#filling in the gender values
print("filling in the gender values")
# Gender column we have 13 missing values
# Use value counts to see data type and distribution  of data
print("Use value counts to see data type and distribution  of data")
print(data_df["Gender"].value_counts())
# fill in with female values
print("fill in with female values")
data_df["Gender"].fillna("Female", inplace=True)
print(data_df["Gender"].value_counts()) # check to see change
print("\n")


#Checking again for missing values
def check_missing_values():
    print("Checking again for missing values")
    print(data_df.isna().sum())
    filtered_row_data = data_df.isna().any(axis=1)
    filtered_df = data_df[filtered_row_data]
    print(filtered_df) #122 rows 
    print("\n")

#filling missing values in the Married columnn
# checking for data distribution in the Married column
print("checking for data distribution in the Married column")
print(data_df["Married"].value_counts())
data_df["Married"].fillna("No", inplace=True)
print(data_df["Married"].value_counts())
#check for any missing values in the married column
print("check for any missing values in the married column")
print(data_df["Gender"].isna().sum())
print("\n")

check_missing_values()

#filling missing values for the dependants column
print("filling missing values for the dependants col")
# missing values = 15
print("check data distribution")
print(data_df["Dependents"].value_counts())
#identify missing indices
missing_indices = data_df[data_df["Dependents"].isna()].index
print(missing_indices)
#generating random values based on the given list
value_list = [1, 2, "3+"]
replacing_values = np.random.choice(value_list, size=len(missing_indices))

#replace values
data_df.loc[missing_indices, "Dependents"] = replacing_values
print(data_df)
print("\n")

check_missing_values()

data_df = data_df.dropna()
print(data_df.isna())
#define  a function that checks for missing values in the given column names and replaces them with the neccessary values

print(data_df.head())
data_df.to_csv("loan_data.csv", index=False)