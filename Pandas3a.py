mean=df['Calories'].mean()
df['Calories'].fillna(value=mean, inplace=True)  #replacing Null values with particular columns mean value
