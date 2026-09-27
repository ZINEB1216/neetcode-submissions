class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        while i <=len(nums) - 1:
            if nums[i] == target:
                return i
                break
            else:
                i = i +1
        return -1