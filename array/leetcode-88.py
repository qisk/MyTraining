class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # nums1,nums2的比较索引值
        nums1_index = m - 1
        nums2_index = n - 1

        # nums1的赋值游标
        nums1_cursor = len(nums1) - 1

        print("nums1_cursor:", nums1_cursor)
        # 时间复杂度O(N^2)
        # nums1和nums2都反向遍历，先取最大的数
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # 从nums2尾部游标位置开始遍历
                if ((j <= nums2_index) and (nums2[j] > nums1[i])):
                    nums1[nums1_cursor] = nums2[j]
                    # 当满足条件时，向左移动游标，以及比较命中的nums2的索引值
                    nums1_cursor = nums1_cursor - 1
                    nums2_index = nums2_index - 1
            # 当满足条件时，向左移动游标，以及比较命中的nums1的索引值
            nums1[nums1_cursor] = nums1[i]
            nums1_cursor = nums1_cursor - 1
            nums1_index = nums1_index - 1

            print("nums1_cursor:", nums1_cursor)

        # 时间复杂度O(N)
        # 如果nums2还没有遍历完，则添加到最头部
        while (nums2_index >= 0):
            nums1[nums1_cursor] = nums2[nums2_index]
            nums1_cursor = nums1_cursor - 1
            nums2_index = nums2_index - 1

        return nums1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    instance = Solution()

    inputList1 = [1,2,3,0,0,0]
    inputList2 = [2,5,6]
    result = instance.merge(inputList1, 3, inputList2, 3)
    print('result=%s'%result)

"""
          i
1,2,3,0,0,0
2,5,6
    j
"""