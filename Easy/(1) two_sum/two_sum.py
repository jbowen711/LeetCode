class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # {value}{index}
        ## loop over nums keep track of index i
        for i in range(len(nums)):
            number = nums[i] ## get value in number
            complement = target - number ## get numbers complement
            if complement in hashMap: ## see if complement exists already in hash
                return [hashMap[complement], i] 
            hashMap[number] = i # if not we add: {number}{i}