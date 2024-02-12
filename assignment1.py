import pandas as pd

df1 = pd.read_csv("./respondent_contact.csv")
df2 = pd.read_csv("./respondent_other.csv")

df3=df1.rename(columns={'respondent_id':'id'})
print(df3)

merge_df = pd.merge(df3,df2,on='id')

cleaned_df = merge_df.dropna()
print(cleaned_df)
cleaned_df.to_csv('cleaned_df.csv')
s_df =cleaned_df[~cleaned_df['job'].str.contains('Insurance')]
ss_df = s_df[~cleaned_df['job'].str.contains('insurance')]

import os
def save_cleaned_data(cleaned_data, output_filename):
    project_folder = "/Users/lixiaoting/Desktop/HKBU_DABE/ECON7035/ECON7035/assignment1"
    output_path = os.path.join(project_folder, output_filename)

    cleaned_data.to_csv(output_path)

output_filename = "cleaned_data.csv"
save_cleaned_data(ss_df, output_filename)





