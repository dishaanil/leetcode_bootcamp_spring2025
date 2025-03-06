class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low = 0
        high = len(nums) -1
        curr =0
        while(curr<=high):
            if(nums[curr] ==0):
                nums[low], nums[curr] = nums[curr], nums[low]
                low += 1
                curr += 1
            elif(nums[curr]==1):
                curr += 1
            else:
                nums[high], nums[curr] = nums[curr], nums[high]
                high -= 1
             
