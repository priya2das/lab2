import pandas as pd

df = pd.read_csv('Cars.csv')

# Q. 1) Instruction ( For Data Cleaning ) -
# Find all Null Values in the dataset. If there is any null value in any column, then fill it with the mean of that column.
print(df.isnull().sum())
df.fillna(df.mean() , inplace = True)
print(df.isnull().sum())

# Q. 2) Question ( Based on Value Counts )-
# Check what are the different types of Make are there in our dataset. And, what is the count (occurrence) of each Make in the data ?
print(df['Make'].unique())
print(df['Make'].value_counts())


# Q. 3) Instruction ( Filtering ) - Show all the records where Origin is Asia or Europe.
print(df[(df['Origin'] == "Asia") | (df['Origin'] == 'Europe')])


# Q. 4) Instruction ( Removing unwanted records ) - Remove all the records (rows) where Weight is above 4000.
df = df[df['Weight'] <= 4000]

# Q. 5) Instruction ( Applying function on a column ) - Increase all the values of 'MPG_City' column by 3.
df_copy = df.copy()
df_copy['MPG_City'] += 3