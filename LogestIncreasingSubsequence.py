def longestIncreasingSubsequence(nums):
    dp = [1]
    for i in range(1, len(nums)):
        dp.append(max([dp[index] + 1 if nums[i] > nums[index] else 1 for index in range(i)]))
    return max(dp)


if __name__ == "__main__":
    print(longestIncreasingSubsequence([20, 1, 3, 9]) == 3)
    print(longestIncreasingSubsequence([20, 1, 3]) == 2)
    print(longestIncreasingSubsequence([20, 1, 3, 9, 4, 5]) == 4)
    print(longestIncreasingSubsequence([20, 20, 20]) == 1)
    print(longestIncreasingSubsequence([1,3,6,7,9,4,10,5,6]) == 6)
