import pandas as pd
from sklearn.model_selection import train_test_split

df_cleaned = pd.read_csv('../../cleaned_data.csv')

# 2. splitting the cleaned data
cleaned_train, cleaned_test = train_test_split(df_cleaned, test_size=0.15, random_state=27)

cleaned_train.to_csv('cleaned_train.csv', index=False)
cleaned_test.to_csv('cleaned_test.csv', index=False)