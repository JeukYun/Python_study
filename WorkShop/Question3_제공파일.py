# --------------------------------------------------------------------------
# 이 파일에서 제공되는 함수와 main() 수정하면 안되며
# 구현으로 표시된 함수를 응시생이 구현하여 프로그램을 완성해야 합니다.
# --------------------------------------------------------------------------

import numpy as np

# #제공 함수 수정 금지
def main():
    # 입력 : 정수 리스트
    num = [9, 2, 7, 6, 20, 9, 2, 1]
    # num = [-5, -3, -1, 9, 4, 2]


    def get_vector(a):
        x = np.array(a)
        k = np.sort(x)
        return k
    # 정수 리스트를 float64 타입의 ndarray 벡터로 변환하고 데이터의 중복없이 내림차순으로 정렬하는 함수 get_vector() 호출 , get_vector()함수 응시생 구현
    result_vector = get_vector(num)

    # 중복제거후 정렬된 벡터 데이터 출력
    print_result(result_vector)


# # 응시생 구현 함수
#  정수 리스트를 float64 타입의 ndarray 벡터로 변환하고 데이터의 중복없이 내림차순으로 정렬하는 기능
#
# @param		num		입력데이터(정수값 리스트)
# @return					1차원 벡터(중복이 제거되고 내림차순으로 정렬된)
def get_vector(num):
    temp_vector = None
    # 응시생 구현 시작
    pass
    # 응시생 구현 끝
    return temp_vector


# #제공 함수 수정 금지
def print_line():
    print("-------------------------------------------------------------------------------")


# #제공 함수 수정 금지
def print_result(data):
    print_line()
    print("중복 제거되고 내림차순으로 정렬된 벡터 데이터 : ", data)
    print_line()


# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
