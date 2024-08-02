import numpy as np
## 기초 수학 연산 및 행렬
import pandas as pd
## 데이터프레임

from sklearn import datasets
## 분류형 가상 데이터 만들기, iris같은 내장 데이터
from sklearn.model_selection import train_test_split
## train, test 데이터 분할

from sklearn.linear_model import LinearRegression
## 선형회귀 분석
from sklearn.linear_model import LogisticRegression
## 로지스틱 회귀분석
from sklearn.naive_bayes import GaussianNB
## 나이브 베이즈
from sklearn import svm
## 서포트 벡터 머신
from sklearn import tree
## 의사결정나무
from sklearn.ensemble import RandomForestClassifier
## 랜덤포레스트

## 분류형 가상 데이터 만들기
from sklearn.datasets import make_classification

X, Y = make_classification(n_samples=1000, n_features=4, n_informative=2, n_redundant=0, random_state=0, shuffle=False)

raw = datasets.load_breast_cancer()
print(raw.feature_names)

data = pd.DataFrame(raw.data)
## 독립변수 데이터 모음
target = pd.DataFrame(raw.target)
## 종속변수 데이터 모음
rawData = pd.concat([data,target], axis=1)
## 독립변수 + 종속변수 열 결합

x = rawData[['mean radius', 'mean texture']]
y = rawData['cancer']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25, random_state=0)
