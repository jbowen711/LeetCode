class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1] * length

        product_to_left = 1
        for i in range(length):
            output[i] = product_to_left
            product_to_left *= nums[i]
        

        product_to_right = 1
        for i in range(length - 1, -1, -1):
            output[i] *= product_to_right
            product_to_right *= nums[i]

        return output