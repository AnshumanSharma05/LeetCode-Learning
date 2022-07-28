class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        summ=0
        
        for i in range(len(accounts)):
            n_sum=0
            for n in range(len(accounts[i])):
                n_sum+=accounts[i][n]
            if n_sum>summ:
                summ=n_sum
        return summ
        