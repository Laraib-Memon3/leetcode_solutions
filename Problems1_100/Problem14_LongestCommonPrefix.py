class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        v=sorted(strs)
        #we can apply brute force appraoc but it is uneffienct becaue we may have long number of string.
        #sort the stirng: flight, flow, flower, now just check first and last string
        first=v[0] #flight
        last=v[-1] #flower
        for i in range(min(len(first), len(last))): #take minimum length of both because prefix can be shortest of both lengths
            if(first[i] != last[i]):
                return ans
            ans+=first[i]
        return ans