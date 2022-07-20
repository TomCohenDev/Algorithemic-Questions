class Solution:
    def romanToInt(self, s: str) -> int:
        
        dic = {'I' : 1 , 'V':5 ,'X':10,'L':50,'C':100,'D':500,'M':1000}

        intNum = 0

        for idx,i in enumerate(s):
            
            intNum += dic[i]
            if idx > 0 and (i != 'I') and (s[idx-1] == 'I' or 'X' or 'C'):
                print(s[idx-1])
                intNum -= 2*dic[s[idx-1]]

        return intNum



test = Solution()

roman = "LV"
print("ROMAN:", roman, "= INT:",test.romanToInt(roman))

"""
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

"""