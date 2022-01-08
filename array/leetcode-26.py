# 数组保序的filter思想
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = 0
        for i in range(len(nums)):
            if (i == 0) or (nums[i] != nums[i - 1]):
                nums[n] = nums[i]
                n = n + 1
        print('nums=%s'%nums[0:n])
        return n


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    instance = Solution()

    inputList = [1, 1, 2, 3, 3]
    result = instance.removeDuplicates(inputList)
    print('result=%s'%result)