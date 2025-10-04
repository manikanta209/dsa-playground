
"""
https://leetcode.com/problems/two-sum/?envType=problem-list-v2&envId=array
"""
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []


if __name__ == '__main__':
    print(twoSum([2, 7, 11, 15], 9))
    print(twoSum([0, 4, 1, 15], 5))




