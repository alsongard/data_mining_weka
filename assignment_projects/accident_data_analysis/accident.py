# this file will be used to clean, extract relevant information and save it to a file that will be later used in weka.

import pandas as pd
import csv 
#load data set
data_df = pd.read_csv("../../data_sets/accidents_2005_to_2007.csv")
print(data_df.head(10))
print(data_df.columns)
print(data_df.shape)



#extracted relevant columns and reduced rows to 5000
new_data_df = data_df.loc[1:50000][["Accident_Severity","Time", "Road_Surface_Conditions", "Weather_Conditions", "Urban_or_Rural_Area", "Number_of_Vehicles"]]
print(new_data_df.shape)
print(new_data_df.columns)
print(new_data_df.isnull().sum()) #returned 48 droping the 48 rows


#cleaning the data
new_data_df = new_data_df.dropna()
print(new_data_df.shape)
print("\n")
#checking the values of urban and rural
print(new_data_df["Urban_or_Rural_Area"].value_counts())
#drop rows containing value 3 in the column Urban_or_Rural_Area

#check values in number of vehicles
print(new_data_df["Number_of_Vehicles"].value_counts())
new_data_df = new_data_df[new_data_df.Urban_or_Rural_Area != 3]
print(new_data_df.shape)

#adding comma to the time column
# new_data_df.Time = ['"' + str(x) + '"' for x in new_data_df.Time]
column_name = "Time"
column_name_2 = "Weather_Conditions"
new_data_df[column_name] = new_data_df[column_name].apply(lambda x : f'"{x}"')
# df[column_name] = df[column_name].apply(lambda x: f'"{x}"')
# df[column_name] = df[column_name].apply(lambda x: '"' + str(x) + '"')
# new_data_df = '"' + new_data_df[column_name] + '"'
new_data_df[column_name_2] = new_data_df[column_name_2].apply(lambda x : f'"{x}"')
print(new_data_df.head)

#checking values of  weather condition s
print(new_data_df["Road_Surface_Conditions"].value_counts())
#create a dictionary for replacements
road_conditions_replacements = {
    "Wet/Damp" : "Wet",
    "Frost/Ice" : "Frost"
}
new_data_df["Road_Surface_Conditions"] = new_data_df["Road_Surface_Conditions"].replace(road_conditions_replacements)
print(new_data_df["Road_Surface_Conditions"].value_counts())

print(new_data_df["Weather_Conditions"].value_counts())
#save to a new csv file
# new_data_df.to_csv("../../data_sets/accidents_2005_to_2007_weka_data.csv",index=False, quoting=csv.QUOTE_NONE)
