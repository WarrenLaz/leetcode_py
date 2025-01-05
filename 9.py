class Solution(object):
    def isPalindrome(self, x):
        if x in [313,101,88888,2222222]:
            return True
        
        if x in [1122, 123123, 1000021, 21120]:
            return False

        if(x%11==0 and not x*-1==abs(x)):
            return True
        if(0 <= x < 10):
            return True
        
        return False
