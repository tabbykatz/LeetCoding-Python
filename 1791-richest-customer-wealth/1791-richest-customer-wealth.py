class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        def runningSum(nums):
            total = 0
            for i in range(len(nums)):
                total += nums[i]
            return total
        wealth = 0
        for account in accounts:
            total = runningSum(account)
            if total > wealth:
                wealth = total
        return wealth