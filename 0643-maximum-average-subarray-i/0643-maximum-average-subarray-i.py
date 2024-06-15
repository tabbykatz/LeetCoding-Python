class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        total = 0
        avg = 0

        for i in range(k):
            total += nums[i]
        avg = total / float(k)
            
        for i in range(k, len(nums)):
            total += nums[i] 
            total -= nums[i - k]
            avg = max(avg, total / float(k))
        return avg

        