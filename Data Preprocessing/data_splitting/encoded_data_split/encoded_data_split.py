import pandas as pd
from sklearn.model_selection import train_test_split

df_encoded = pd.read_csv('../../encoding_data.csv')  
# df_encoded = pd.read_csv('Data Preprocessing/encoding_data.csv') 
# 1. splitting and save the encoded data
# simply split the data into training and testing sets (85/15 split)
encoded_train, encoded_test = train_test_split(df_encoded, test_size=0.15, random_state=27)

# Save the training & test data to CSV files
encoded_train.to_csv('encoded_train.csv', index=False)
encoded_test.to_csv('encoded_test.csv', index=False)