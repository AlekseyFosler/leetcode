from leetcode.easy.longest_common_prefix import Solution


def test_longest_common_prefix():
    solution = Solution()

    assert solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""
