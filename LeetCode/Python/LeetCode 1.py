# Easy Problem
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_indices = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement], index]
            num_indices[num] = index

        return []  # Return an empty list if no such indices are found

# Example usage:
nums = [2, 7, 11, 15]
target = 9

sol = Solution()
result = sol.twoSum(nums, target)