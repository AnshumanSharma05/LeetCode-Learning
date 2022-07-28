class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        for i in range(len(nums)):
            sum=0
            for n in range(i+1):
                sum+=nums[n]
            l.append(sum)
        return l