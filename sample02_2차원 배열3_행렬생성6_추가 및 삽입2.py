import numpy as np
print(np.__version__)


arr = np.array([[1,2,3],[4,5,6]])
'''
[[1 2 3]
 [4 5 6]]
'''

print("색인 :", arr[...,0]) #[1 4]
print("색인 :", arr[...,[0]]) # >> shape을 유지함
'''
[[1]
 [4]]
'''

xxx = np.insert(arr, 0,  [[100],[200]], axis=1)
print(xxx)
'''
[[100 200   1   2   3]
 [100 200   4   5   6]]
'''
xxx = np.insert(arr, [0], [[100],[200]], axis=1)
print(xxx)
'''
[[100   1   2   3]
 [200   4   5   6]]
'''