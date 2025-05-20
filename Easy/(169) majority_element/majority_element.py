class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = {} ## create dictionary
        for number in nums: 
            majority[number] = majority.get(number, 0) + 1 ## add frequency of nums frequency, number {number , frequency}

        maxFrequency = max(majority.values()) ## return max frequency

        for key, value in majority.items(): ## loop key and value if value == maxFrequency return the number associated
            if value == maxFrequency:
                return key