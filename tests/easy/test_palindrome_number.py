
from leetcode.easy.palindrome_number import Solution


def test_two_sum():
    solution = Solution()

    assert solution.isPalindrome(121) is True
    assert solution.isPalindrome(-121) is False
    assert solution.isPalindrome(10) is False
