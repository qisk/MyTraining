class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data.append(x)

    def pop(self):
        """
        :rtype: None
        """
        self.data.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.data[len(self.data) - 1]

    def min(self):
        """
        :rtype: int
        """
        return min(self.data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)

    # 返回 -3.
    print('minStack.min():%s' % minStack.min())

    minStack.pop()

    # 返回 0.
    print('minStack.top():%s' % minStack.top())
    # 返回 -2.
    print('minStack.min():%s' % minStack.min())
