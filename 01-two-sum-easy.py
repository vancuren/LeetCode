# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# You can return the answer in any order.

from typing import List


class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashed = {}
        answer = None
        
        i=0
        while i < len(nums):
            if target >= 0:
                if nums[i] <= target:
                    hashed[nums[i]] = i
            if target < 0:
                if nums[i] >= target:
                    hashed[nums[i]] = i 
            i+=1
            
        j=0
        while j < len(nums) and not answer:
            if target - nums[j] in hashed.keys():
                if hashed[target - nums[j]] != j:
                    answer = [j, hashed[target - nums[j]]]
                    break
            j+=1
                
        
        return answer
    
    
if __name__ == "__main__":
    solution = Solution()
    print('Answer', solution.twoSum([2,7,11,15], 9))    
    print('Answer', solution.twoSum([3,2,4], 6))
    print('Answer', solution.twoSum([3,3], 6))

