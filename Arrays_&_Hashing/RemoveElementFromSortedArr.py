
"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=problem-list-v2&envId=array
"""

from typing import List


def removeDuplicates(nums: List[int]) -> int:

        if not nums:
            return 0

        unique_count = 1
        current_index = 1

        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                nums[current_index] = nums[i]   #override the array with new elements
                current_index += 1
                unique_count += 1

        return unique_count

if __name__ == '__main__':
    print(removeDuplicates([1, 1, 1, 2, 2, 2]))