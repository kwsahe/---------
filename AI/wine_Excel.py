from sklearn.datasets import load_wine
import pandas as pd

# 와인 데이터셋 로드
wine = load_wine()

# 특징 데이터와 타겟 데이터 추출
X = pd.DataFrame(wine.data, columns=wine.feature_names)
y = pd.Series(wine.target, name='target')

# 특징 데이터와 타겟 데이터를 하나의 데이터프레임으로 결합
df = pd.concat([X, y], axis=1)

# 데이터프레임을 엑셀 파일로 저장
file_path = "wine_dataset.xlsx"
df.to_excel(file_path, index=False)

print(f"데이터셋이 '{file_path}'에 저장되었습니다.")
