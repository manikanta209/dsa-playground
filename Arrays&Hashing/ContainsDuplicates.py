from typing import List

from sympy import false


def hasDuplicate( nums: List[int]) -> bool:
    seen = set()            # To store numbers we've already seen
    for num in nums:
        if num in seen:     # if already seen, duplicate found
            return True
        seen.add(num)
    return False


if __name__ == '__main__':
    print(hasDuplicate([2, 7, 11, 3]))

    """
    Short answer :
    return len(nums)!=len(set(nums))
    """

    """ Other solution: But it will be time consuming
    # n = len(nums)
    # 
    # for i in range(n):
    #     for j in range(i+1, n):
    #         if nums[i] == nums[j]:
    #             return True
    # 
    # return false

    """