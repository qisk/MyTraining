class Solution(object):
    def isValid(self, s):
        valid_result = True

        # 新建一个符号栈
        op_stack = []
        for i in range(len(s)):
            # 判断是否是左括号
            flag_push = self.isLeft(s[i])

            if flag_push:
                # 是左括号就插入栈
                op_stack.append(s[i])
            else:
                # 是右括号就尝试出栈，判断栈顶元素是否为左括号
                flag_pop = self.isMatch(op_stack[len(op_stack) - 1], s[i])
                if flag_pop:
                    # 是左括号就出栈
                    op_stack.pop(len(op_stack) - 1)
                else:
                    # 如果左右括号不匹配，就退出循环
                    valid_result = False
                    break

        # 如果栈中还有元素，说明不合法
        if valid_result and len(op_stack) > 0:
            valid_result = False

        return valid_result

    def isLeft(self, s):
        if s == "(" or s == "[" or s == "{":
            return  True
        else:
            return False

    def isMatch(self, left, right):
        if left == "(" and right == ")":
            return True
        if left == "[" and right == "]":
            return True
        if left == "{" and right == "}":
            return True

        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    instance = Solution()

    # result = instance.isValid("()")
    # print('result=%s' % result)

    result = instance.isValid("()[]{}")
    print('result=%s' % result)

    result = instance.isValid("(]")
    print('result=%s' % result)

    result = instance.isValid("([)]")
    print('result=%s' % result)

    result = instance.isValid("{[]}")
    print('result=%s' % result)
