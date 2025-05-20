class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {} ##create hashMap - pythonDictionary 
        if len(s) != len(t): ## if lengths unequal its not an Anagram
            return False
        
        for char in s: ## Add frequencies to counter using sage get method
            counter[char] = counter.get(char, 0) + 1      
        
        for char in t: ## check t letter in s
            if char not in counter:
                return False
            counter[char] -= 1 ## decrease frequency based on t letter
            if counter[char] < 0: ## t frequency is larger than s return false
                return False
        return True ## anagram!