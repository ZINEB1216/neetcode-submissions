class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupes = {}
        for mot in strs:
            signature = "".join(sorted(mot))   
            if signature not in groupes:
                groupes[signature] = []        
            groupes[signature].append(mot)      
        return list(groupes.values())          