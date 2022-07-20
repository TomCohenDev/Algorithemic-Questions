import random

class Solution:
    def isPalindrome(self, x: int) -> bool:
        print(x)

        # start at 0 for the lowest digit
        done = False
        idx = 0
        backNum = 0
        xList = []

        # make a list from x
        while not done:
            backNum = int((x/10**idx)%10)
            if backNum == 0 and (x/10**idx)<1:
                done = True
                break     
            xList.append(backNum)
            idx+=1
        # compare the end of the list to the front
        for i in range(len(xList)):
            if xList[i] != xList[-(1+i)]:
                return False
            

        return True

test = Solution()


def testPalindrom():
    
    i = 0
    done = False
    while not done:
        print("=======")
        print("TEST Number", i)
        done = test.isPalindrome(random.randint(0,100000000000))
        print(done)
        i += 1
    
        
        


testPalindrom()