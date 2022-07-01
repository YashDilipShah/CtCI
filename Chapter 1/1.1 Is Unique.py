"""
IS UNIQUE : Implement an algorithm to deteremine if a string has all unique 
characters. What if you cannot use additional data structures.  
"""

"""
Leetcode #217
217. Contains Duplicate
Easy

Given an integer array nums, return true if any value appears at least twice in 
the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true

Example 2:

Input: nums = [1,2,3,4]
Output: false

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

 

Constraints:

    1 <= nums.length <= 105
    -109 <= nums[i] <= 109


"""

class Solution:
    def containsDuplicate(self, nums) -> bool:
        set_num = set(nums)
        return len(set_num) < len(nums)