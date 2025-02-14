# Three sum triplet finding with target value as 0. Also the triplet pairing should not have duplicate

# it works the same way of two sum but the *no duplicate* part is tricky
from typing import List
class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n= len(nums)
        target = 0
        result = []

        for idx, val in enumerate(nums):
            # skip duplicate
            if idx > 0 and val == nums[idx - 1]:
                continue

            l = idx + 1
            r = n - 1
            required_sum = target - val
            while l < r:
                if nums[l] + nums[r] == required_sum:
                    result.append([nums[idx], nums[l], nums[r]])
                    # the result shouldn't have duplicate too 
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < required_sum:
                    l += 1
                else:
                    r -= 1
        return result
    
if __name__ == "__main__":
    print(Solution().threeSum([-1,0,1,2,-1,-4]))