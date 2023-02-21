tren_codes

#import library
import pandas as pd

#import data
df= pd.read_csv('/Users/fad/Downloads/Project_Ads/DA_11.5.4_Dataset_trending_by_time.csv')

#drop duplicates if any
df.drop_duplicates()

#check missing values
df.isna().sum()

#change data types
df['trending_date'] = pd.to_datetime(df['trending_date'], format= '%Y-%m-%d %H:%M:%S')

#import data 
df.to_csv('/Users/fad/Downloads/Project_Ads/DA_11.5.4_Dataset_trending_by_time_clean.csv')