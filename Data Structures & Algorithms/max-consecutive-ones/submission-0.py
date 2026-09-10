class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maximum = 0
        for i in nums:
            if(i==0):
                count=0
            else:
                count+=1
                if(count>maximum):
                    maximum=count  
        return maximum
        