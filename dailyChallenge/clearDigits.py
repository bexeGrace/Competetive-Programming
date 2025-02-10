class Solution:
    def clearDigits(self, s: str) -> str:
        numS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        curr = 0
        while curr < len(s):
            if s[curr] in numS:
                s = s[:curr-1] + s[curr+1:] 
                curr -= 1
            else:
                curr += 1
        
        return s