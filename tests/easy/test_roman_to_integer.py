from leetcode.easy.roman_to_integer import Solution


def test_roman_to_integer():
    solution = Solution()

    assert solution.romanToInt("III") == 3
    assert solution.romanToInt("LVIII") == 58
    assert solution.romanToInt("MCMXCIV") == 1994
