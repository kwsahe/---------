# NumPy 튜토리얼

NumPy는 파이썬에서 고성능 수치 계산을 가능하게 하는 라이브러리로, 다차원 배열 객체와 다양한 수학 함수들을 제공함.

## NumPy 설치

NumPy를 설치하려면 다음 명령어를 사용함:

```sh
pip install numpy
```

## NumPy 시작하기
NumPy를 사용하려면 먼저 라이브러리를 임포트해야 함:

```python
import numpy as np
```

## 배열 생성
```python
#리스트로부터 배열 생성
import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a)

#다차원 배열 생성
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

#배열의 크기 확인
print(a.shape)  # (5,)
print(b.shape)  # (2, 3)

# 배열의 데이터 타입
print(a.dtype)  # int64

c = np.array([1.0, 2.0, 3.0])
print(c.dtype)  # float64

```

## 배열 연산
```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(x + y)  # [5 7 9]
print(x - y)  # [-3 -3 -3]
print(x * y)  # [ 4 10 18]
print(x / y)  # [0.25 0.4  0.5 ]

# 브로드캐스팅
d = np.array([1, 2, 3])
print(d + 1)  # [2 3 4]

```
## 유용한 함수들
```python
print(np.zeros((2, 3)))  # [[0. 0. 0.]
                         #  [0. 0. 0.]]
print(np.ones((2, 3)))   # [[1. 1. 1.]
                         #  [1. 1. 1.]]
print(np.eye(3))         # [[1. 0. 0.]
                         #  [0. 1. 0.]
                         #  [0. 0. 1.]]

print(np.arange(0, 10, 2))   # [0 2 4 6 8]
print(np.linspace(0, 1, 5))  # [0.   0.25 0.5  0.75 1.  ]

```

## 배열 인덱싱 및 슬라이싱
```python
# 인덱싱
e = np.array([1, 2, 3, 4, 5])
print(e[0])  # 1
print(e[4])  # 5

# 슬라이싱
print(e[1:3])  # [2 3]
print(e[:2])   # [1 2]
print(e[2:])   # [3 4 5]

# 다차원 배열 인덱싱 및 슬라이싱
f = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f[0, 0])  # 1
print(f[1, :])  # [4 5 6]
print(f[:, 2])  # [3 6 9]
```

## 배열 연산 함수
```python
print(np.sum(f))    # 45
print(np.mean(f))   # 5.0
print(np.max(f))    # 9
print(np.min(f))    # 1

print(np.sum(f, axis=0))  # [12 15 18]
print(np.sum(f, axis=1))  # [ 6 15 24]


```

