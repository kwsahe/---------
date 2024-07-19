from sklearn.datasets import load_iris
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. 데이터 수집 및 로드
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names

# 2. 데이터 전처리
df = pd.DataFrame(X, columns=feature_names)
df['target'] = y
print("데이터프레임의 처음 5행:")
print(df.head())

# 학습용 데이터와 테스트용 데이터로 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 데이터 정규화
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 3. 모델 선택 및 초기화
model = RandomForestClassifier(n_estimators=100, random_state=42)

# 4. 모델 학습
model.fit(X_train, y_train)

# 5. 모델 평가
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'모델 정확도: {accuracy:.2f}')
print("분류 보고서:")
print(classification_report(y_test, y_pred))

# 6. 모델 사용
new_data = [[5.1, 3.5, 1.4, 0.2]]  # 새로운 데이터 예시 (Iris-setosa의 특징 값)
new_data_scaled = scaler.transform(new_data)  # 정규화 적용
predicted_class = model.predict(new_data_scaled)
print(f'예측된 붓꽃 종류: {iris.target_names[predicted_class][0]}')
