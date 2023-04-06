from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
# Support Vector Machine's 
from sklearn.svm import SVC

classifier = SVC()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

# Summary of the predictions made by the classifier
print(classification_report(y_true, y_pred))
print(confusion_matrix(y_true, y_pred))
# Accuracy score
from sklearn.metrics import accuracy_score
print('accuracy is',accuracy_score(y_pred,y_true))

# Do at least two visualizations to describe or show correlations in the Glass Dataset.
import seaborn as sns   #For Visualisation import seaborn library
import matplotlib.pyplot as plt
sns.barplot(x = glass['Type'], y = glass['Ca'])

sns.catplot(data=glass, x="Type", y="K")
sns.regplot(x="Type", y="Fe", data=glass);
