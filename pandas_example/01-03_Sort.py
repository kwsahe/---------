import pandas as pd

data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [25, 32, 18, 47],
        'city': ['New York', 'Paris', 'London', 'San Francisco']}
df = pd.DataFrame(data)

df.sort_values('age', inplace=True)
# print(df)

df.set_index('name', inplace=True)
# print(df)

df.reset_index('name', inplace=True)
print(df)


# 오름차순으로 정렬하기
# df.sort_values('열 이름')

# 내림차순으로 정렬하기
# df.sort_values('열 이름', ascending=False)