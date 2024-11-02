import pandas as pd
from sklearn.model_selection import train_test_split

def split_data(test_size=0.15):
    # Read the data from CSV
    # pay attention to change the path in the final integration phase
    df_encoded = pd.read_csv(r'../../../Data Preprocessing/encoding_data.csv')
    
    # Perform train-test split
    train_df, test_df = train_test_split(df_encoded, test_size=test_size, random_state=27)
    
    # Save the split data to new CSV files
    train_df.to_csv('../data/train_data.csv', index=False)
    test_df.to_csv('../data/test_data.csv', index=False)
    
split_data()