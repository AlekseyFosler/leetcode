"""
14. Longest Common Prefix
Easy
15.2K
4.1K
Companies
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        resp = ""
        minimum_length = len(strs[0])
        for s in strs[1:]:
            minimum_length = min(minimum_length, len(s))

        for i in range(0, minimum_length):
            current = strs[0][i]
            for j in range(0, len(strs)):
                if strs[j][i] != current:
                    return resp
            resp += current
        return resp
