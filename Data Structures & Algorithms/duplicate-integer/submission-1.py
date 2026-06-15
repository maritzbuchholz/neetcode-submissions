class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = list(set(nums))
        if len(nums) == len(dups):
            return False
        else:
            return True
        