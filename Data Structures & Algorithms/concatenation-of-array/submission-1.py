class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            ans.append(nums[i])
        for j in range(n):
            ans.append(nums[j])
        return ans


        