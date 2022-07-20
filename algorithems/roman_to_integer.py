class Solution:
    def romanToInt(self, s: str) -> int:
        
        intNum = 0
        done = False



        for idx,i in enumerate(s):

            
            if s[idx] == "I": 
                intNum += 1
                

            elif s[idx] == "V":
                intNum += 5
                if idx > 0 and s[idx-1] == "I":
                    intNum -= 2

            elif s[idx] == "X":
                intNum += 10
                if idx > 0 and s[idx-1] == "I":
                    intNum -= 2

            elif s[idx] == "L":
                intNum += 50
                if idx > 0 and s[idx-1] == "X":
                    intNum -= 20

            elif s[idx] == "C":
                intNum += 100
                if idx > 0 and s[idx-1] == "X":
                    intNum -= 20

            elif s[idx] == "D":
                intNum += 500
                if idx > 0 and s[idx-1] == "C":
                    intNum -= 200

            elif s[idx] == "M":
                intNum += 1000
                if idx > 0 and s[idx-1] == "C":
                    intNum -= 200

            
            
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

