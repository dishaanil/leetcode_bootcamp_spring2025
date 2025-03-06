class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        #need left and right pointer
        left_pointer = 0
        right_pointer = len(numbers) - 1
        res = []
        #loop, left pointer at start and right pointer at end 
        while left_pointer < right_pointer:
            current_sum = numbers[left_pointer] + numbers[right_pointer]
         # if the sum is equal to target return the indexes
            if current_sum == target:
                return [left_pointer + 1, right_pointer + 1]
        # if the sum of the left and right pointer is > target, decrease index of right pointer
            elif current_sum > target:
                right_pointer -= 1
        #if the sum of the left and right pointer is < target, increase index of left pointer
            else:
                left_pointer += 1 
        return []
