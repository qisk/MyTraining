class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # 声明一个栈List,仅存储数字, pop()用于出栈，append用于入栈
        stack = []
        for i in range(len(tokens)):
            if not self.isOp(tokens[i]):
                # 如果是数字，就入栈
                temp = int(tokens[i])
                stack.append(temp)
                print("stack.append:", tokens[i])
            else:
                # 如果是操作符，先将两个数字出栈，计算结果后再入栈
                y = stack.pop()
                x = stack.pop()
                print("stack.pop:", x, y, tokens[i])
                result_val = self.calVal(x, y, tokens[i])
                print("result:", result_val)
                stack.append(result_val)
        return stack[0]

    def isOp(self, str):
        if str == "+" or str == "-" or str == "*" or str == "/":
            return True
        else:
            return False

    def calVal(self, x, y, op):
        if op == "+":
            return x + y
        elif op == "-":
            return x - y
        elif op == "*":
            return x * y
        elif op == "/":
            # python是向下取整，这里使用浮点除法再加上int，实现向零取整
            return int(x / float(y))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    instance = Solution()

    tokens = ["2", "1", "+", "3", "*"]
    result = instance.evalRPN(tokens)
    print('result=%s'%result)