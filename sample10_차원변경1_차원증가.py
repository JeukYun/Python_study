import numpy as np
print(np.__version__)

'''
    1. 차원 증가 ( 1차원 --> 2차원 )
    예> [1 2 3] shape : (3, ) == > [[1 2 3]] shape : (1,3)
    
    가. arr1D.reshape((행, 열))
    나. np.expand_dims(arr1D, axis = 0)
    다. arr1D[np.newaxis, ...]
        arr1D[np.newaxis, :]
'''
# 가. arr1D.reshape((행, 열))
arr1D = np.array([1, 2, 3])
print(arr1D, arr1D.shape) # [1 2 3] (3, )

arr2D = arr1D.reshape((1,3)) # (1, -1)로 주어도 됨
# arr2D = arr1D.reshape((1,-1))
print(arr2D, arr2D.shape) # [[1 2 3]] (1, 3)

# 나. np.expand_dims
arr1D = np.array([1, 2, 3])
arr2D = np.expand_dims(arr1D, axis=0)
print(arr2D, arr2D.shape) #[[1 2 3]] (1, 3)

# 다. arr1D[np.newaxis, ...]
arr1D = np.array([1, 2, 3])
arr2D = arr1D[np.newaxis, ...]
print(arr2D, arr2D.shape) # [[1 2 3]] (1, 3)