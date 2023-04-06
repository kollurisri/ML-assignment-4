import seaborn as sns   #For Visualisation import seaborn library
import matplotlib.pyplot as plt
sns.barplot(x = train_df['Sex'], y = train_df['Survived']) 
