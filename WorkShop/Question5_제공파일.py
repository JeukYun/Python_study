# --------------------------------------------------------------------------
# 이 파일에서 제공되는 함수와 main() 수정하면 안되며
# 구현으로 표시된 함수를 응시생이 구현하여 프로그램을 완성해야 합니다.
# --------------------------------------------------------------------------

import numpy as np


# #제공 함수 수정 금지
def main():
    # 입력 : 임의의 정수 리스트
    num = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    # num = [[21, 22], [31, 41], [65, 46], [7, 8], [19, 10]]
    print(np.array(num))
    x = np.array(num)
    a = x[:, 0]
    b = x[:,1]


    print("a = x[:,1] :", a)
    print("b = x[:,0] :", b)

    a.shape = (-1,1)
    b.shape = (-1,1)
    print(b)
    #print(np.insert(a,1,axis = 1))
    #   (5 X 2) 리스트를 ndarray 행렬로 변환하고 변환된 ndarray 행렬에서 1열과 2열의 순서를 바꾸는 함수 get_matrix() 호출 , get_matrix()함수 응시생 구현
    result_matrix = get_matrix(num)

    # 1열과 2열 교환후 행렬 데이터를 출력
    print_result(result_matrix)


# # 응시생 구현 함수
#  (5 X 2) 리스트를 ndarray 행렬로 변환하고 변환된 ndarray 행렬에서 1열과 2열의 순서를 바꾸는 기능
#
# @param		num		입력데이터(정수 리스트)
# @return				    1열과 2열의 순서가 바뀐 2차원 행렬
def get_matrix(num):
    temp_matrix = None
    # 응시생 구현 시작
    pass
    # 응시생 구현 끝
    return temp_matrix


# #제공 함수 수정 금지
def print_line():
    print("-------------------------------------------------------------------------------")


# #제공 함수 수정 금지
def print_result(data):
    print_line()
    print("1열과 2열의 순서가 바뀐 행렬 데이터: \n", data)
    print_line()


# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
