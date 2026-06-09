class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        num = 0
        for i in range(len(nums) - 1):
            if nums[i]==nums[i+1]:
                num=num+1
        if num>0:
            return True
        else:
            return False       
            
        