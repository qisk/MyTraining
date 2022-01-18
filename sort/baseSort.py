class Solution(object):
    def bubbleSort(self, inputlist, length):
        if length <= 1:
            return inputlist
        for i in range(len(inputlist)):
            # 判断是否进行交换
            flag = False
            for j in range(0, length - i - 1):
                if inputlist[j] > inputlist[j + 1]:
                    tmp = inputlist[j]
                    inputlist[j] = inputlist[j + 1]
                    inputlist[j + 1] = tmp
                    flag = True
            if not flag:
                # 如果没有交换，说明已经是有序的，可以退出循环
                break
        return inputlist

    def insertionSort(self, inputlist, length):
        if length <= 1:
            return inputlist
        for i in range(1, len(inputlist)):
            # 要插入的数，从索引1开始
            value = inputlist[i]
            # 从前面的有序区间中，依次进行比较，如果前序区间的值比value大，就交换位置
            # 如果前序区间的值比value小，循环结束，可以移动游标i
            j = i - 1
            while j >= 0:
                if inputlist[j] > value:
                    inputlist[j + 1] = inputlist[j]
                    inputlist[j] = value
                    j = j - 1
                else:
                    break
            #  print('inputlist:%s' % inputlist)
        return inputlist


if __name__ == '__main__':
    instance = Solution()

    # 冒泡排序
    testlist = [4, 3, 6, 3, 2, 1]
    sortedList = instance.bubbleSort(testlist, len(testlist))
    print(sortedList)

    # 插入排序
    testlist = [4, 3, 6, 3, 2, 1]
    sortedList = instance.insertionSort(testlist, len(testlist))
    print(sortedList)

