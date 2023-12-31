from leetcode.easy.two_sum import Solution


def test_two_sum():
    solution = Solution()

    assert solution.twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1]
    assert solution.twoSum(nums=[3, 2, 4], target=6) == [1, 2]
    assert solution.twoSum(nums=[3, 3], target=6) == [0, 1]
    assert solution.twoSum(nums=[3, 2, 3], target=6) == [0, 2]
