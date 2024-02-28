class Solution:

    def runningSum(self, nums: list[int]) -> list[int]:
        outputList = []
        i = 0
        for n in nums:
            i += n
            outputList.append(i)

        return outputList


def main():
    print(Solution().runningSum([5, 8, 6, 4]))


if __name__ == "__main__":
    main()
