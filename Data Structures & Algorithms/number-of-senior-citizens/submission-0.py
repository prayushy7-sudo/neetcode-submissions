class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c=0
        for i in range(len(details)):
            if int(details[i][-4]+details[i][-3])>60:
                c+=1
        return c        
                
        