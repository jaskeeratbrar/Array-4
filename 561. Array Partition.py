## T(C) : O(nlogn) + O(n) i.e ===> O(nlogn)
## S(C) : O(1)

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()

        print(nums)

        sum = 0

        for i in range(1,len(nums), 2):
            sum += min(nums[i], nums[i-1])
        
        return sum






        
