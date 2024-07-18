import pandas as pd

data_df = pd.read_csv("../../data_sets/political_data.csv")

print(data_df.info())

#select data attributes for data analysis -> given in readme file
data_df = data_df[["_unit_id","_trusted_judgments", "_last_judgment_at", "audience", "bias", "bias:confidence", "message", "message:confidence", "bioid", "source", "text"]]
print(data_df.head(10))

# data cleaning
#check for any missing values
print(data_df.isnull().sum()) # result missing values in 15 rows  and 4 rows for text

#drop these rows
df_cleaned = data_df.dropna()

#recheck for missing values
print(df_cleaned.isnull().sum())  # no missing values

# convert to text file
df_cleaned.to_csv("../../data_sets/cleaned_political_data.csv", index=False)
