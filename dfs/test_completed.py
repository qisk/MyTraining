from copy import deepcopy


def isSame_test(self, strList, n, i):
    # 测试isSame_release中为什么要用while，而不能直接比较strList[n]和strList[i]返回？
    # 可以使用strList['h', 'a', 'a']来模拟，h和第一个a交换，h和第二个a交换，最后的叶子节点，都是相同的，
    # 所以要去用while进行去重处理，不仅判断交换的两个元素(n,i)是否相同，还要判断和n后面的元素是否存在相同的情况。
    # 测试代码
    if (n < i) and strList[n] == strList[i]:
        return True
    return False


def isSame_release(self, strList, n, i):
    # 正确代码
    while n < i:
        print("while:", strList, n, i)
        if strList[n] == strList[i]:
            print("isSame return True:", strList, n, i)
            return True
        n = n + 1
    print("isSame return False:", strList, n, i)
    return False


class Solution(object):
    count = 0

    def getAllCombination(self, strList, sameFunc):
        size = len(strList)
        n = 0
        result = []
        self.exec(strList, size, n, result, sameFunc)
        return result

    def exec(self, strList, size, n, result, sameFunc):
        print("exec index=%s, sameFunc=%s" % (self.count, sameFunc))
        self.count = self.count + 1
        # 递归什么时候结束
        if n == size - 1:
            result.append(deepcopy(strList))
            print("exec return result:%s" % result)
            return

        # 递归要做的事情
        for i in range(n, size):
            # 判断要交换的两个数是否一样，如果一样就无需进行交换，继续下一个循环
            if sameFunc(self, strList, n, i):
                continue
            self.swap(strList, i, n)
            print("swap begin:", strList)
            print("exec begin:", size, n + 1)
            self.exec(strList, size, n + 1, result, sameFunc)
            print("exec end:", size, n + 1, result)
            self.swap(strList, i, n)
            print("swap end:", strList)

    def swap(self, strList, i, n):
        if i == n:
            return
        tmp = strList[n]
        strList[n] = strList[i]
        strList[i] = tmp

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    instance = Solution()
    result = instance.getAllCombination(['h', 'a', 'a'], isSame_test)
    print("result len:%d, %s" % (len(result), result))
    result = instance.getAllCombination(['h', 'a', 'a'], isSame_release)
    print("result len:%d, %s" % (len(result), result))
