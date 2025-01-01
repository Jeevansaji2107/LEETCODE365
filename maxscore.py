class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        one_count = s.count('1')

        count = 0
        score = 0

        for i in range(n - 1):
            if s[i] == '1':
                one_count -= 1
            else:
                count += 1
            score = max(score, count + one_count)

        return score

