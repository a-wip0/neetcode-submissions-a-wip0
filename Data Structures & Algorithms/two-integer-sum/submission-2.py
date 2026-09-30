class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}

        for k, v in enumerate(nums):
            diff = target - v
            if diff in temp:
                return [temp[diff], k]
            else:
                temp[v] = k
        
        return []