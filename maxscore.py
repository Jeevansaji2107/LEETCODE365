class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        one_count = s.count('1')

        zero_count = 0
        max_score = 0

        for i in range(n - 1):
            if s[i] == '1':
                one_count -= 1
            else:
                zero_count += 1
            max_score = max(max_score, zero_count + one_count)

        return max_score

