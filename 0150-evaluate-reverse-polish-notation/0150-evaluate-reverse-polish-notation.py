class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operations = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": lambda a, b: int(a / b)}
        for i in range(len(tokens)):
            stack.append(tokens[i])
            if tokens[i] in operations.keys():
                operation = stack.pop()
                operand2 = int(stack.pop())
                operand1 = int(stack.pop())
                result = operations[operation](operand1, operand2)
                stack.append(result)
        return int(stack[-1])
        