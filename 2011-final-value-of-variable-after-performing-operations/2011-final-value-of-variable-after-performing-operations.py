class Solution(object):
    def finalValueAfterOperations(self, operations):
        value = 0
        for i in range(len(operations)):
            if (operations[i] == '++X') or (operations[i] == 'X++'):
                value += 1
            elif (operations[i] == '--X') or (operations[i] == 'X--'):
                value -= 1
        return value