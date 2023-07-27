import numpy as np
print(np.__version__)

'''
     1. ndarray 추가

      문법:
        arr = np.append(arr, values, axis=None)

      - 추가된 새로운 배열을 반환
      - axis=None 이면 flatten 된후에 추가된다.


     2. ndarray 삽입

       문법:                        색인
         arr = np.insert(arr, idx|fancy|slice, value,  axis ).

         - fancy 사용시 value와 shape가 일치해야 된다.
'''

#  1. ndarray 추가
#  np.append(arr,  value,  axis )
arr = np.array([9,8,7,5,4,3])
new_arr = np.append(arr, [1,2,3])
print(arr)       # [9 8 7 5 4 3]
print(new_arr)   # [9 8 7 5 4 3 1 2 3]

#  2. ndarray 삽입
#  np.insert(arr, idx|fancy, value,  axis )

# 가. idx 이용
arr = np.array([9,8,7,5,4,3])
new_arr = np.insert(arr, 0, [1,2,3]) # 0 번째에 1,2,3 삽입
print(arr)  # [9 8 7 5 4 3]
print(new_arr)  # [1 2 3 9 8 7 5 4 3]

# 나. fancy 이용
arr = np.array([9,8,7,5,4,3])
new_arr = np.insert(arr, [0,3,1], [1,2,3])  # 0->1 , 3->2, 1->3 삽입됨. 따라서 갯수가 일치해야 된다.
print(arr)        #  [9 8 7 5 4 3]
                  #   1 9 8 7 5 4 3  <- 0에 1 삽입후
                  #   1 9 8 7 2 5 4 3  <- 3에 2 삽입후
                  #   1 9 3 8 7 2 5 4 3  <- 1에 3 삽입
print(new_arr)    #  [1 9 3 8 7 2 5 4 3]

#  다. slice 이용
arr = np.array([9,8,7,5,4,3])
new_arr = np.insert(arr, np.s_[0:2], [1,2])
print(arr)  # [9 8 7 5 4 3]
            #  1 9 8 7 5 4 3 <- 0에 1 삽입후
            #  1 9 2 8 7 5 4 3 <- 1에 2 삽입후
print(new_arr)  # [1 9 2 8 7 5 4 3]