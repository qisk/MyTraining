class Solution(object):
    def func(self, list):
        size = len(list)
        n = 0
        result = []
        exec(list, size, n, result)
        return result

    def exec(self, list, size, n, result):
        # 递归什么时候结束
        if n == size - 1:
            result.append(list)
            return

        # 递归要做的事情
        for i in list(range(n, size)):
            if isSame(list, n, i):
                continue
            swap(list, i, n)
            exec(list, size, n + 1, result)
            swap(list, i, n)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    instance = Solution()
    result = instance.func(['h', 'a', 't'])
    print("result:%s" % result)
