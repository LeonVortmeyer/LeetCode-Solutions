#My LeetCode Exercises

#-------------------Problem 9 - Palindrome Number------------------------------------
"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        nums = [int(d) for d in str(x)]
        reversed_nums = [None] * len(nums)
        start = 0
        stop = len(nums) - 1
        print(nums)
        while start < stop:
            reversed_nums[start], reversed_nums[stop] = nums[stop], nums[start]
            start += 1
            stop -= 1

        if len(nums) % 2 == 1:
            reversed_nums[(len(nums) // 2)] = nums[(len(nums) // 2)]

        print(reversed_nums)

        if reversed_nums == nums:
            return True

        return False

#-------------------Problem 35 - Search Insert Position------------------------------------
"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
"""


class Solution(object):
    def searchInsert(self, nums, target):
        if not nums: return 0

        low, high = 0, len(nums) - 1

        if target in nums:
            return nums.index(target)
        else:
            while True:
                mid = (low + high) // 2
                if nums[low] <= target <= nums[high]:
                    if target <= nums[mid]:
                        high = mid - 1
                    elif target >= nums[mid]:
                        low = mid + 1
                else:
                    if target < nums[low]:
                        return low
                    else:
                        return high + 1


#-------------------Problem 50 - Search Insert Position------------------------------------
"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""


class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1 / x, -n)  # if n < 0, return power of 1/x

        partial = self.myPow(x, n // 2)  # recusively call on n // 2 to solve in log(n) time
        result = partial * partial

        if (n % 2) == 1:  # if n mod 2 is 1 then multiply result by another x
            result *= x
        return result
