import numpy as np
print(np.__version__)

'''
   

'''
# 1. np.zeros((행, 열))
print("1. np.zeros((행,열)):")
data = np.zeros((2,3))
# data = np.zeros((2,3), dtype=np.int32)
print(data, data.dtype)

# 2. np.ones((행, 열))
print("2. np.ones((행, 열)):")
data = np.ones((2, 3))
# data = np.ones((2, 3), dtype=np.int32)
print(data , data.dtype)

# 3. np.empty((행, 열))
print("3. np.empty((행, 열))")
data = np.empty((2, 3))
data = np.empty((2, 3), dtype=np.int32)
print(data , data.dtype )

# 4. np.full((행, 열), 값)
print("4. full((행, 열), 값)")
data = np.full((2, 3), 10)
print(data)