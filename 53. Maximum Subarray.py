## T(C)  --  O (n)
## S(C) -- O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

            ## Maximum Subaarray
    
        trackerHighestSub = nums[0]
        findNextHigherSub = nums[0]
    
        for i in nums[1:]:
            findNextHigherSub = max(i, findNextHigherSub + i)
            trackerHighestSub = max(findNextHigherSub, trackerHighestSub)

        return trackerHighestSub
