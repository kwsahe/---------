import sklearn
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris

iris=load_iris()
dir(iris)

feature_names = iris.feature_names
print("Feature names: ", feature_names)

X = iris.data
y = iris.target

df = pd.DataFrame(X, columns=feature_names)
df['target'] = y

print("데이터프레임: ")
print(df.head())


# data : 피처의 데이터 세트

# target : 분류 시 레이블 값, 회귀 시 숫자 결과값 데이터 세트

# target_names : 개별 레이블의 이름 (*레이블 : 모델이 맞추려는 목표)

# feature_names : 피처의 이름 (*피쳐 : 데이터의 속성,열(column)의 개념이라고 이해)

