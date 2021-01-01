from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            j = target - nums[i]
            if len(result) != 2:
                if j != nums[i] and j in nums:
                    result.append(i)
                elif j == nums[i]:
                    try:
                        second_occurance_index = nums.index(nums[i], i + 1)
                    except ValueError:
                        pass
                    else:
                        return [i, second_occurance_index]
        return result


a = Solution()
number = [3,3]
t = 6
# a.twoSum(number, t)
print(a.twoSum(number, t))

# print(dict(enumerate(number)))

