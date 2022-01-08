# 数组保序的filter思想
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = 0
        # 时间复杂度O(2 * N)
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[n] = nums[i]
                n = n + 1
        #  将0补在最后
        while n < len(nums):
            nums[n] = 0
            n = n + 1

        return nums


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    instance = Solution()

    inputList = [0, 1, 0, 3, 12]
    result = instance.moveZeroes(inputList)
    print('result=%s'%result)