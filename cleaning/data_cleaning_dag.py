import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('/data/AmesHousing.csv')
print(df.shape)
print(df.info())