class Solution(object):
    def isHappy(self, n):
        seen = set()
        while (n not in seen and n != 1):
            seen.add(n)
            digits = (int(char) for char in str(n))
            total = 0
            for digit in digits:
                total += digit*digit
            n = total
        return n == 1