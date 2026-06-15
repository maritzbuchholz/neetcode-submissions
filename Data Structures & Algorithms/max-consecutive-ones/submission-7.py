class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cons = 0
        a1 = 0
        a0 = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                a1 += 1
            else:
                if a1 > cons:
                    cons = a1
                a1 = 0
        if a1 > cons:
            cons = a1
        return cons