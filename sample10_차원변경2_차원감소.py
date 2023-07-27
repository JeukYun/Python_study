import numpy as np
print(np.__version__)

'''
    2. 차원 감소 ( n차원 --> n-1차원 )
    예> [[1 2 3]] shape : (1,3) ==> [1 2 3] shape : (3, ) 
        np.squeeze(arr2D, axis = 0)
'''

arr2D = np.arange(3).reshape(1,3)
print(arr2D, arr2D.shape) #[[0 1 2]] (1, 3)

arr1D = np.squeeze(arr2D, axis=0)
print(arr1D, arr1D.shape) #[0 1 2] (3,)