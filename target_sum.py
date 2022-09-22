# How many combinations can you make with operators +, - to make the target value given
# You are already given the array with x amount of elements
# Code uses decesion trees
# recursive function
# https://www.youtube.com/watch?v=g0npyaQtAQM

def find_target_sumways(nums: List[int], target: int) -> int:
    dp = {} # (index, total) -> #mof ways

    def backtrack(i, total):
        if i == len(nums):
            return 1 if total == target else 0
        if (i, total ) in dp:
            return dp[i, total]

        dp=[(i, total)] = (backtrack(i + 1, total + nums[i]) +
                            backtrack(i + 1, total - nums))
