import pandas as pd

data = [['A', 1], ['B', 2], ['C', 3]]
df = pd.DataFrame(data, columns=['col1', 'col2'])
print(df)

data = {'col1' : ['A', 'B', 'C'], 'col2' : [1, 2, 3]}
df = pd.DataFrame(data)
print(df)

# df = pd.read_csv('data.csv')
# print(df)

# 열 추가
df['col3'] = [4, 5, 6]

df.drop('col3', axis=1, inplace=True)
# axis 파라미터는 삭제할 기준을 지정함.
# axis=0이면 행을 삭제함.
# axis=1이면 열을 삭제함.

# inplace 파라미터는 변경 사항을 원본 데이터프레임에 직접 적용할지를 지정함.
# inplace=True로 설정하면 원본 데이터프레임인 df가 직접 수정됨.
# inplace=False 또는 생략하면 원본 데이터프레임은 변경되지 않고, 수정된 새로운 데이터프레임이 반환됨.

# 행 추가
df.loc[3] = ['D', 4, 5]
df.drop(3, inplace=True)

# 열 이름 변경
df.rename(columns={'col1': 'new_col1'}, inplace=True)