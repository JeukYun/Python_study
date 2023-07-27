import numpy as np
print(np.__version__)

'''
   np.arrange + reshape ( 중요 )
   

'''

print("1. arange(10)")
#arange([start,] stop[, step,], dtype=None, *, like=None)
data = np.arange(10).reshape((2,5)) # 0~ 9 까지 데이터를 (2행, 5열)로
print(data)

arr = np.array([1,2,3,4,5,6])
print(arr)
print(arr.reshape(6,1))

