// Given an array of integers nums and an integer target, 
// return indices of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution,
// and you may not use the same element twice.

// You can return the answer in any order.

class Solution {

    twoSum(nums, target) {

        let hashed = {};
        let answer = null;

        let i=0;
        while (i < nums.length) {
            if (target >= 0) {
                if (nums[i] <= target) {
                    hashed[nums[i]] = i
                }
            }
            if (target < 0) {
                if (nums[i] >= target) {
                    hashed[nums[i]] = i
                }
            }
            i++;
        }

        let j=0;
        while (j < nums.length && !answer) {
            if (hashed[target - nums[j]] && hashed[target - nums[j]] != j) {
                    answer = [j, hashed[target-nums[j]]]
                    break
            }
            j++;
        }

        return answer;

    }

}


solution = new Solution();
console.log('Answer', solution.twoSum([2,7,11,15], 9))
console.log('Answer', solution.twoSum([3,2,4], 6))
console.log('Answer', solution.twoSum([3,3], 6))
