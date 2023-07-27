import numpy as np
print(np.__version__)

'''
    np.linspace(start, stop, [num=50, endpoint=True])
        => [start,stop] 범위사이의 값을 num개 생성, 기본 type은 float64, num 값을 지정하지 않으면 기본은 50
        => 랜덤값 추출이 아닌 지정 범위사이 균일한 간격으로 추출
        => 기본적으로 stop값이 범위에 포함됨.  interval [`start`, `stop`].
            포함시키지 않을려면  endpoint=False 로 지정한다. Default is True.
'''

print("1. np.linspace(0, 1, 11)")
# 0 <= 값 <= 1 사이의 값을 11개 생성
data = np.linspace(0, 1, 11 )
print(data, data.dtype)  # [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1. ]   float64

print("2. np.linspace(0, 0.9, 10)")
# 0 <= 값 <= 0.9 사이의 값을 10개 생성
data = np.linspace(0, 0.9, 10)
print(data) # [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]
