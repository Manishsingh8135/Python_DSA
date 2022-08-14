class Solution:
    def subarraySum(self, nums, k) :
        dict = {0: 1}

        total, res = 0, 0
        for num in nums:
            total += num
            diff = total - k

            res += dict.get(diff, 0)
            dict[total] = 1 + dict.get(total, 0)
        return res

sol=Solution()
nums = [1,2,3]
k = 3
x=sol.subarraySum(nums,k)
print(x)