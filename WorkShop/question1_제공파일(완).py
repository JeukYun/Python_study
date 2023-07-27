# --------------------------------------------------------------------------
# 이 파일에서 제공되는 함수와 main() 수정하면 안되며
# 구현으로 표시된 함수를 응시생이 구현하여 프로그램을 완성해야 합니다.
# --------------------------------------------------------------------------
import numpy as np


# #제공 함수 수정 금지
def main():
    # 입력: 배열 데이터 (0 ~ 29까지의 1차원 배열)
    #arr_data = np.arange(30)
    arr_data=np.arange(5, 35)

    def change_2d_array(a, b, c):
        k = a.reshape(b,c)
        s = np.sum(k,axis=0)[0:1]
        return s

    # 1차원 배열을 2차원(5,6)배열로 변환 후 변환된 배열의 각 행의 첫 번째 열의 합을 계산하는
    # 함수 change_2d_array() 호출
    # change_2d_array() 함수 응시생 구현
    result = change_2d_array(arr_data, 5, 6)
    
    # 계산된 각 행의 첫 번째 열의 합을 출력
    print_result(result)


# # 응시생 구현 함수
# 1차원 배열을 2차원배열로 변환 후 변환된 배열의 각 행의 첫 번째 열의 합을 계산하는 기능
#
# @param      arr            입력데이터(1차원 배열데이터)
# @param      row           입력데이터(2차원 배열의 행)
# @param      column      입력데이터(2차원 배열의 열)
# @return                       변환된 배열의 각 행의 첫 번째 열의 합
def change_2d_array(arr, row, column):
    # 응시생 구현 시작
    pass
    # 응시생 구현 끝

# #제공 함수 수정 금지
def print_line():
    print("-------------------------------------------------------------------------------")


# #제공 함수 수정 금지
def print_result(result):
    print_line()
    print("각 행의 첫열의 합: ", result)
    print_line()


# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()

