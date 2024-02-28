class Solution:
    def twoSum(self, nums: list[int], target: int) -> dict[int]:
        numMap = {}
        i = 0
        for num in nums:
            numMap[i] = num
            i += 1
        return numMap


def main():
    print(Solution().twoSum([0, 2, 3], 5))
    print(Solution().twoSum([2, 7, 11, 15], 9))
    print(Solution().twoSum([3,2,4], 6))
    print(Solution().twoSum([3,3], 6))


if __name__ == "__main__":
    main()
