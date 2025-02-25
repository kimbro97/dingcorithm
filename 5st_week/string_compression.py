input = "abcabcabcabcdededededede"


def string_compression(s):
    if len(s) == 1:
        return 1

    min_length = float('inf')

    for unit in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[:unit]
        count = 1

        for i in range(unit, len(s), unit):
            if s[i:i+unit] == prev:
                count += 1
            else:
                compressed += str(count) + prev if count > 1 else prev
                prev = s[i:i+unit]
                count = 1

        compressed += str(count) + prev if count > 1 else prev

        min_length = min(min_length, len(compressed))

    return min_length


print(string_compression(input))  # 14 가 출력되어야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))



# aabbaccc => 2a2ba3c