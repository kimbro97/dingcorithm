def solution(arr):
    answer = []
    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1]:
            answer.append(arr[i])
    answer.append(arr[-1])
    return answer


def solution_stack(arr):
    stack = []
    for num in arr:
        if not stack or stack[-1] != num:
            stack.append(num)
    return stack