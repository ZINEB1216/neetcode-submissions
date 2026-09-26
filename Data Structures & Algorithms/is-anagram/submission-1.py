class Solution:         
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted = "".join(sorted(s))
        t_sorted = "".join(sorted(t))
        if len(s_sorted) == len(t_sorted):
            for i in range(len(s_sorted)):
                if s_sorted[i] != t_sorted[i]:
                    return False
            return True
        else:
            return False