class Solution:
    def minArray(self, numbers):
        min_index = 0

        for i in range(len(numbers) - 2):
            if numbers[i] > numbers[i + 1]:
                min_index = i + 1
                break
        return numbers[min_index]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    instance = Solution()

    # inputList = [3, 4, 5, 1, 2]
    inputList = [2, 2, 2, 0, 1]
    result = instance.minArray(inputList)
    print('result=%s' % result)
