class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split()
        words.reverse()
        return " ".join(words)


solution = Solution()


print("Output = blue is sky the, " + "Result = " + solution.reverseWords("the sky is blue"))
print("Output = world hello, " + "Result = " + solution.reverseWords("  hello world  "))
print("Output = example good a, " + "Result = " + solution.reverseWords("a good   example"))
