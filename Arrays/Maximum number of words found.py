class Solution(object):
    def mostWordsFound(self, sentences):
        
        final_sum=1
        for i in sentences:
            new_sum=1
            
            for n in i:
                if n==" ":
                    new_sum+=1
            if new_sum>final_sum:
                final_sum=new_sum
        return final_sum
            