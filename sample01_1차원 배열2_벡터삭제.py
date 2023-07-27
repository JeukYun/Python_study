import numpy as np
print(np.__version__)

'''
    1. ndarray 삭제
          문법:
        arr = np.delete(arr, idx|fancy|slice, axis ) #axis는 2차원 부터 사용(행, 열중 어떤거 삭제 할 것인지)
      - 순방향, 역방향 모두 가능하다.
      - 삭제된 새로운 배열을 반환 (in-place가 False)
      - axis=None 이면 flatten 적용됨. ==> 다차원이 1차원으로
      - slice인 경우에는  np.s_[::2]  형식 사용한다.
      
     2. 값으로 삭제
      - np.where( (arr==5) | (arr==8)) 활용하여 일치하는 인덱스를 먼저 찾고 삭제한다.
      - np.delete(arr, np.where())
    

'''

# 1. idx|fancy|slice 삭제
print("1. idx로 삭제")
arr = np.array([9,8,7,5,4,3])
new_arr = np.delete(arr,0)
print(arr)       # [9 8 7 5 4 3]
print(new_arr)   # [8 7 5 4 3]

print("2. fancy 삭제") #[idx, idx2, idx3, ...] 여러 idx 지정하는 방식, python에는 없는 방식임./numpy만 지원
arr = np.array([9,8,7,5,4,3])
new_arr = np.delete(arr, [0,3,5] ) # fancy 인덱싱 (정수배열 인덱싱)
print(arr)       # [9 8 7 5 4 3]
print(new_arr)   # [8 7 4]

print("3. slice 삭제,  np.s_[::2]")
arr = np.array([9,8,7,5,4,3])
new_arr = np.delete(arr, np.s_[0:4] ) # slice 삭제, np.s_가 꼭 붙어야 함.
print(arr)       # [9 8 7 5 4 3]
print(new_arr)   # [4 3]

# 2. 값으로 삭제하는 방법
arr = np.array([9,8,7,5,4,3])
xx = np.delete(arr, np.where(arr == 5)) # 5 값 삭제,
print(arr) #[9 8 7 5 4 3]
print(xx) # [9 8 7 4 3]

print(np.where(arr == 5)) # (array([3], dtype=int64),) >> 3번째에 5라는 값이 있다
print(np.where((arr == 5)|(arr==8))) # (array([1, 3], dtype=int64),) >> 1번째, 3번째에 5 또는 8 값이 있다

arr = np.array([9,8,7,5,4,3])
xx = np.delete(arr, np.where((arr==5)|(arr==8))) # 5 와 8 값 삭제,
print(arr) #[9 8 7 5 4 3]
print(xx) # [9 7 4 3]