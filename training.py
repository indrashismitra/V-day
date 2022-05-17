from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.tree import DecisionTreeRegressor
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.utils.multiclass import unique_labels

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

def decisiontreeclassifier(X_train,y_train):
    dtc = DecisionTreeRegressor()
    dtc.fit(X_train, y_train)
    return dtc

def randomforestclassifier(X_train,y_train):
    rfc = RandomForestClassifier(n_estimators=100,criterion='gini')
    rfc.fit(X_train,y_train)
    return rfc

def kneighborsclassifier(X_train,y_train):
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train,y_train)
    return knn

def svmclassifier(X_train,y_train):
    svm = svm.SVC(kernel="linear") 
    svm.fit(X_train, y_train)
    return svm

def mlpclassifier(X_train, y_train):
    mlp = MLPClassifier()
    mlp.fit(X_train, y_train)
    return mlp