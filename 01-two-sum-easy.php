<?php

class Solution {
    
    // function constructor() {}

    public function twoSum($nums, $target) {
        
        $hashed = [];
        $answer = null;

        $i = 0;
        while ($i < count($nums)) {
            if ($target >= 0) {
                if ($nums[$i] <= $target)  {
                    $hashed[$nums[$i]] = $i;
                }
            }
            if ($target < 0) {
                if ($nums[$i] >= $target)  {
                    $hashed[$nums[$i]] = $i;
                }
            }
            $i++;
        }

        $j = 0;
        while($j < count($nums) && !isset($answer)) {
            if ($hashed[$target - $nums[$j]] && $hashed[$target - $nums[$j]] != $j) {
                $answer = [$j, $hashed[$target - $nums[$j]]];
                break;
            }
            $j++;
        }

        return $answer;
    }
}

$solution = new Solution;
print_r($solution->twoSum([2,7,11,15], 9));
print_r($solution->twoSum([3,2,4], 6));
print_r($solution->twoSum([3,3], 6));