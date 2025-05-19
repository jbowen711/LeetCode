class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = {} ## make hashmap
        for i in range(len(nums)): ## loop over nums
            number = nums[i] ## get curr num
            if number in hashMap: ## check if it exists in hashMap
                return True 
            hashMap[number] = i ## otherwise add it to hashMap
        return False  