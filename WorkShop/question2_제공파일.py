# --------------------------------------------------------------------------
# 이 파일에서 제공되는 함수와 main() 수정하면 안되며
# 구현으로 표시된 함수를 응시생이 구현하여 프로그램을 완성해야 합니다.
# --------------------------------------------------------------------------
import numpy as np


# #제공 함수 수정 금지
def main():
    # 입력: 배열 데이터 (임의의 값이 저장된 1차원 배열)
    a_arr = np.array([9,5,4,-3,7,0,12,76,88] )
    b_arr = np.array([66,7,4,0,-4,-7,-22,-90,100])

    # a_arr = np.array([6, 5, 8, 3, 1, 34, -2, -5, 9])
    # b_arr = np.array([9, 8, 7, 6, 1, 34, -2, -5, 9])
    A = a_arr.reshape(3, 3)
    B = b_arr.reshape(3, 3)
    print(A == B)

    #def check_difference(a, b):
    #    a = np.array([])
    #    x = a.reshape(3,3)
    #    y = b.reshape(3,3)
    #    np.append(a, x)
    #    return a



    # (3,3) 행렬로 변환후 두 행렬간의 값을 비교하여 일치하면 0, 일치하지 않으면 1로 설정하는 함수
    # check_difference() 호출, check_difference() 함수 응시생 구현
    result_arr = check_difference(a_arr, b_arr)

    # 두 행렬간 비교결과값의 (3,3) 행렬 출력
    print_result(result_arr)


# # 응시생 구현 함수
# (3,3) 행렬로 변환후 두 행렬간의 값을 비교하여 일치하면 0, 일치하지 않으면 1로 설정하는 함수
#
# @param      arr1       입력데이터(1차원 배열데이터)
# @param      arr2       입력데이터(1차원 배열데이터)
# @return                    (3,3) 행렬
def check_difference(arr1, arr2):
    # 응시생 구현 시작
    pass
    # 응시생 구현 끝


# #제공 함수 수정 금지
def print_line():
    print("-------------------------------------------------------------------------------")


# #제공 함수 수정 금지
def print_result(arr):
    print_line()
    print("(3,3) 행렬 :\n", arr)
    print_line()


# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()

