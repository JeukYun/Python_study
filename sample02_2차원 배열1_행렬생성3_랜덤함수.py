import numpy as np
print(np.__version__)

'''
   

'''

# 1) 랜덤값 고정
np.random.seed(1234)

# 2) np.random.random(size = (행, 열)
print("1. random(size = (행, 열)")
#arr = np.random.random()
arr = np.random.random(size = (2, 4)) # 튜플로 넣음
print(arr,type(arr), arr.dtype) #<class 'numpy.ndarray'> float64

# 3) np.random.rand(행, 열)
'''
    def rand(*dn: Any) -> Any
    rand(d0, d1, ..., dn)
'''
print("2. rand(행,열)")
arr = np.random.rand(2, 4)          # 튜플이 아님을 주의
print(arr,type(arr), arr.dtype) #<class 'numpy.ndarray'> float64

# 3) np.random.randn([갯수])
# 표준편차가 1이고 평균값이 0인 정규분포에서 표본 추출. 갯수 생략하면  1개반환
print("3. randn(행, 열)")
arr = np.random.randn()
arr = np.random.randn(2,3)
print(arr)

# 4) np.random.randint(low, high, size = (행, 열))
# 주어진 최소/최대 범위 안에서 임의의 난수 n개 추출
print("4. randint(1,10, size = (행, 열))")
arr = np.random.randint(1,10, size = (2, 3))
print(arr)

# 4) np.random.randint(high, size=(행, 열))
# 0 ~ 최대(exclusive) 범위안에서 임의의 정수 n개 반환, 복원추출 (뽑고 다시 넣는거)
print("4. randint(5, size=(행, 열)): ")
arr = np.random.randint(5, size=(2,3))
print(arr)

print("5. randint(0,300, size=(행, 열)): ")
rr = np.random.randint(0,300, size=(5,3))
print(rr)