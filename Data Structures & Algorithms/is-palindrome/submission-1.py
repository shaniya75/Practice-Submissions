class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=s.lower()
        y=''
        for i in x:
            if i.isalnum():
                y+=i
        print(y)
        if y[::-1]==y:
            return True
        else:
            return False
        