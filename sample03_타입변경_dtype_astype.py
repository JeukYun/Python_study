import numpy as np
print(np.__version__)

'''
    타입변경
    ==> 다차원 배열의 모든 요소가 한꺼번에 변경된다. ( 벡터화 연산 )
    1. dtype 속성
    
    2. astype 함수 이용 -- ( 중요 )
'''

# 1. int --> float으로
data = [10,20,30]
arr1 = np.array(data)

arr2 = np.array(data , dtype=np.float64) #가. dtype 속성
arr3 = arr1.astype(np.float64)           #나. astype 함수 이용

print("1. 원본 데이터: ", arr1.dtype , arr1)  # int32 [10 20 30]
print("2. int값을 float으로 변경 1: ", arr2.dtype , arr2)  # float64 [10. 20. 30.]
print("2. int값을 float으로 변경 2: ", arr3.dtype , arr3)  # float64 [10. 20. 30.]

# 2. float --> int 으로
data = [10.5,20.7,30.23, 100] # 정수(100)가 있어도 upcasting으로 실수로 반환
arr1 = np.array(data)
arr2 = np.array(data , dtype=np.int64)  #가. dtype 속성
arr3 = arr1.astype(np.int64)            #나. astype 함수 이용
print("3. 원본 데이터: ", arr1.dtype , arr1)  # float64 [10.5  20.7  30.23]
print("4. float 값을 int 으로 변경 1: ", arr2.dtype , arr2) # int64 [10 20 30]
print("4. float 값을 int 으로 변경 2: ", arr3.dtype , arr3) # int64 [10 20 30]
print()

# 3. int --> bytes , str
data = [10,20,30]
arr1 = np.array(data)
arr2 = np.array(data , dtype=np.string_)  # bytes 타입,  np.string 안됨.
arr3 = arr1.astype(np.string_)
arr4 = np.array(data , dtype=np.str_)   # str 타입
arr5 = arr1.astype(np.str_)
print("5. 원본 데이터: ", arr1.dtype , arr1)  # int32 [10 20 30]
print("6. int 값을 bytes 으로 변경 1: ", arr2.dtype , arr2) # |S2 [b'10' b'20' b'30']
print("6. int 값을 bytes 으로 변경 2: ", arr3.dtype , arr3) # |S11 [b'10' b'20' b'30']
print("7. int 값을 str 으로 변경 : ", arr4.dtype , arr4) # <U2 ['10' '20' '30']
print("7. int 값을 str 으로 변경 : ", arr5.dtype , arr5) # <U11 ['10' '20' '30']

# print(dir(np))


# 4. str --> int
data =['10','20','30']
arr1 = np.array(data)
arr2 = arr1.astype(np.int32)
print("8. str 값을 int 으로 변경 :",arr2) # [10 20 30]

arr3 = np.array(data).astype(np.int32) # 권장하는 방식
print(arr3) # [10 20 30]

