import numpy as np
print(np.__version__)

'''
    1. 다차원 열병합
        1) np.hstack((arr, arr2)) ==> 수평(horizontal)방향으로 병합
        2) np.concatenate((arr,arr2), axis=1 ) ==> axis=1인 컬럼방향으로 병합
        3) np.column_stack((arr, arr2)) ==> 컬럼(column)방향으로 병합

    2. 다차원 행병합
       1) np.vstack((arr, arr2)) ==> 수직(vertical)방향으로 병합
       2) np.concatenate((arr,arr2), axis=0 ) ==> axis=0인 행방향으로 병합
       3) np.row_stack((arr, arr2)) ==> 행(row)방향으로 병합
'''
# 1. 다차원 열병합
arr = np.arange(9).reshape(3,3)
arr2 = arr * 2
print(arr)
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
'''

print(arr2)
'''
[[ 0  2  4]
 [ 6  8 10]
 [12 14 16]]
'''
# 튜플형태로 들어가야 함을 명시..!
column_merge = np.hstack((arr,arr2)) # 열병합이지만 h임을 주의
column_merge2 = np.concatenate((arr,arr2) , axis=1)
column_merge3= np.column_stack((arr, arr2))
print(column_merge)


# 2. 다차원 행병합
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
'''
print(arr2)
'''
[[ 0  2  4]
 [ 6  8 10]
 [12 14 16]]
'''
row_merge = np.vstack((arr,arr2))
row_merge2 = np.concatenate((arr,arr2) , axis=0)
row_merge3= np.row_stack((arr, arr2))
print(row_merge)
