import numpy as np
print(np.__version__)

'''
   

'''
arr1 = [[1,2,3],[4,5,6]]
arr2D = np.array(arr1)

print("1. 행렬의 차원(dimension,axis)갯수:", vector1.ndim) # 1
print("2. 행렬의 각 차원의 크기(shape)-매우중요:", vector1.shape) # tuple로 반환 (3,)
print("3. 행렬의 총 요소 갯수(size):", vector1.size)   # 3
print("4. 행렬의 저장 데이터 type(dtype):", vector1.dtype) # int32 (4 byte )