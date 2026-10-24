class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        dictionnaire = {}
        for num in nums:
            if num in dictionnaire:
                dictionnaire[num] += 1
            else:
                dictionnaire[num] = 1
        while len(result) < k:
            result.append(max(dictionnaire, key=dictionnaire.get))
            del dictionnaire[max(dictionnaire, key=dictionnaire.get)]
        return result