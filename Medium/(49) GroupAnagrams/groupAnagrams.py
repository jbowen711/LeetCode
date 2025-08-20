class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = defaultdict(list) ##init defaultdict so no key errors
        for word in strs: ## iterate over list of strs
            wordSorted = ''.join(sorted(word)) ## sortWord and put back together
            anagramDict[wordSorted].append(word) ## use sortedWord to store anagrams
        return list(anagramDict.values()) ##return all values in a list
       