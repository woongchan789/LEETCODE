class Solution(object):
    def fib(self, n):
        fib_list = [0, 1, 1]
        if n <= 2:
            return fib_list[n]
        else:
            start = 1
            for i in range(1,n-1):
                fib_list.append(fib_list[i] + fib_list[i+1])
        return fib_list[n]