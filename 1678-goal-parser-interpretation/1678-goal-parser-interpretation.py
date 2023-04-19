class Solution(object):
    def interpret(self, command):
        while '()' in command:
            command = command.replace('()', 'o')
        while '(al)' in command:
            command = command.replace('(al)', 'al')
        return command