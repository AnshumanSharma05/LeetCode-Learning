class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        for n in range(2):
            
            for i in range(len(nums)):
                l.append(nums[i])
            n+=1
        return l        