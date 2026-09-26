class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string
        s = s.lower().translate(str.maketrans("", "", string.punctuation)).replace(" ", "")
        limit = len(s)//2
        c = 0
        while c <= limit and len(s) != 0:
            if s[c] != s[-c-1]:
                return False
            else:
                c = c+1
        return True