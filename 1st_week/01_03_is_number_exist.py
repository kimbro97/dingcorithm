def is_number_exist(number, array):
    for i in array:
        if number == i:
            return True

    # 이 부분을 채워보세요!
    return False


result = is_number_exist
print("정답 = True 현재 풀이 값 =", result(3, [3,5,6,1,2,4]))
print("정답 = Flase 현재 풀이 값 =", result(7, [6,6,6]))
print("정답 = True 현재 풀이 값 =", result(2, [6,9,2,7,1888]))

"""
반복문으로 배열을 순회한다
순회하면서 특정값이 있는지 없는지 판단한다
특정값이 없으면 FALSE
특정값이 있으면 True를 린턴한다
"""