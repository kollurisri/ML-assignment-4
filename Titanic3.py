# To implement naive bayes on Titanic data set, first we need to preprocess the data
#Data Preprocessing
#Removing few features from the raw data
train_df = train_df.drop(['Ticket', 'Cabin','Parch','SibSp', 'Name', 'PassengerId'], axis=1)
test_df = test_df.drop(['Ticket', 'Cabin','Parch','SibSp', 'Name'], axis=1)
combine = [train_df, test_df]

for dataset in combine:
    dataset['Sex'] = dataset['Sex'].map( {'female': 1, 'male': 0} ).astype(int)  #Converting Categorical Feature
    
    print(train_df.isnull().sum())   #Checking any Null values present in the dataset
    train_df['Embarked'].describe()
    #Replacing missing values in Embarked Column
common_value = 'S'
data = [train_df, test_df]

for dataset in data:
    dataset['Embarked'] = dataset['Embarked'].fillna(common_value)
    ports = {"S": 0, "C": 1, "Q": 2}
data = [train_df, test_df]

for dataset in data:
    dataset['Embarked'] = dataset['Embarked'].map(ports)
    meanAge = int(train_df.Age.dropna().mean())
print('Mean Age = ', meanAge)
#Replacing missing values in Age column with mean and in Fare column with median
for dataset in combine:
    dataset['Age'] = dataset['Age'].fillna(meanAge)
    dataset['Fare'] = dataset['Fare'].fillna(test_df['Fare'].dropna().median())
    from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
X_train = train_df.drop('Survived', axis=1)
y_train = train_df['Survived']
X_test  = test_df.drop('PassengerId', axis=1).copy()
gaussian = GaussianNB() 
gaussian.fit(X_train, Y_train)  
Y_pred = gaussian.predict(X_test)  
gaussian.score(X_train, Y_train)
