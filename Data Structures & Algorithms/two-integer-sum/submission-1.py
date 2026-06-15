class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}

        for k, v in enumerate(nums):
            diff = target - v
            if diff in data:
                return [data[diff], k]
            
            data[v] = k