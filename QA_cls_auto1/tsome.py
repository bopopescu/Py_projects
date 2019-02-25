def test_three(self, nums):
    def two_pointer(nums, target):
        '''two pointer technique and it is caller responsibility to pass proper nums'''
        first = 0
        second = len(nums) - 1
        two_sums = []
        while first < second:
            two_sum = nums[first] + nums[second]
            if two_sum < target:
                first += 1
            elif two_sum > target:
                second -= 1
            else:
                two_sums.append([nums[first]] + [nums[second]])
                while first + 1 < len(nums) and nums[first] == nums[first + 1]:
                    first += 1
                while second - 1 >= 0 and nums[second] == nums[second - 1]:
                    second -= 1
                first += 1
                second -= 1
        return two_sums

    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums = sorted(nums)
    three_sums = []
    i = 0
    while i < len(nums) - 2:
        two_sums = two_pointer(nums[i + 1:], -nums[i])
        for j in range(len(two_sums)):
            three_sums.append([nums[i]] + two_sums[j])
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        i += 1
    return three_sums