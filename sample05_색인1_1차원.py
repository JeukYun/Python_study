import numpy as np
print(np.__version__)

'''
    1차원 배열(벡터) 색인
    
    1. python의 인덱싱/슬라이싱 모두 가능
    2. fancy 색인
    3. boolean 색인
        ==> 반드시 색인 대상과 길이가 같아야 한다.
        ==> python 의 and/or/not 대신 & | ~ 사용한다. 
    
'''
x = [0,1,2,3,4,5,6,7,8,9]
print(x)
arr = np.arange(10)
print(arr)
#[0 1 2 3 4 5 6 7 8 9]

# 1. 인덱싱 (순방향, 역방향)
print(arr[0], arr[-1])

# 2. 슬라이싱
print(arr[1:5]) #[1 2 3 4]
print(arr[:5]) #[0 1 2 3 4]
print(arr[1:]) #[1 2 3 4 5 6 7 8 9]
print(arr[1:10:2]) #[1 3 5 7 9]
print(arr[:]) #[0 1 2 3 4 5 6 7 8 9]
print(arr[...]) #[0 1 2 3 4 5 6 7 8 9]

# 3. fancy 색인 : [idx, idx2 ....]
data = np.arange(10) * 100
print("1. original: ", data) # [  0 100 200 300 400 500 600 700 800 900]
# print(data[1,3,5]) : 주의할 것
print("2. data[[1,3,5]]: ", data[[1,3,5]]) # [100 300 500]
print("3. data[[8,1,5]]: ", data[[8,1,5]]) # [800 100 500]

# 4. boolean 색인 => 반드시 색인 대상과 길이가 같아야 한다.
data = np.array([1,2,3,4,5])
print("1. original: " , data)
print("2. 벡터연산,  data%2==0: " , data%2==0) # [False  True False  True False]
print("3. boolean 색인, [True,True,True,True,False]: ",
      data[[True,True,True,True,False]]) # [1 2 3 4]

print("4. boolean 색인 활용,data[data%2==0]: ",data[data%2==0])  # [2 4]
print("5. boolean 색인 활용,data[data > 3 ]: ",data[data > 3])  # [4 5]
print("6. boolean 색인의 & 연산자: " , data[(data%2==0) & (data >2)]) # [4]
print("7. boolean 색인의 | 연산자 " , data[(data%2!=0) | (data < 4)]) # [1 2 3 5]
print("8. boolean 색인 ~ 연산자: ",data[~(data > 3)])  # [1 2 3]


# 실습 : 특정 이름 검색
names = np.array(["세종","홍길동","이순신","정조","홍길동"])
# 가. boolean 색인
print(names == "홍길동")  # [False  True False False  True]
print(names[names == "홍길동"])
print(names[[False, True, False, False, True]])
# 나. list comprehension
print([x for x in names if x == '홍길동'])


