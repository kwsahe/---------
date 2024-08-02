import seaborn as sns
import pandas as pd

# from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# iris = load_iris()
# X = iris.data
# 데이터 값
# y = iris.target  
# 라벨, 학습시 목적값

iris = sns.load_dataset('iris')

X = iris.drop('species', axis=1)
y = iris['species']

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print('Accuracy: ', accuracy)

# k-NN 알고리즘이 작동하는 방식은 시험 데이터 포인트와 가장 가까운 학습 데이터 포인트를 찾는 것입니다. 따라서 시험 데이터 포인트의 예측 결과인 결과값은 가장 가까운 학습 데이터 포인트의 결과값과 같게 됩니다.





