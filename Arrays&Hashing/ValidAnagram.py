
"""
https://leetcode.com/problems/valid-anagram/submissions/1790843818/

1. If length is not equal then return
2. Store the count in the HashMap or dict
3. if the count is not equal then return False
"""
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    counts, countT = {}, {}

    for i in range(len(s)):
        counts[s[i]] = 1 + counts.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    for c in counts:
        if counts[c] != countT.get(c, 0):
            return False

    return True


if __name__ == '__main__':
    print(isAnagram("cat","dog"))


"""
Another solution: But it will take more memory
    return sorted(s) == sorted(t)
"""