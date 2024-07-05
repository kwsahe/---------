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

