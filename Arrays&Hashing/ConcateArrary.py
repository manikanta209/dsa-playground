from typing import List

"""
https://leetcode.com/problems/concatenation-of-array/description/?status=AC&page=1
"""

def getConcatenation(nums: List[int]) -> list[int]:
    return nums + nums


if __name__ == '__main__':
    print(getConcatenation([2, 7, 11, 15]))