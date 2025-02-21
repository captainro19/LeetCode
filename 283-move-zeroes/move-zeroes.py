class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        NextNonZero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[NextNonZero], nums[i] = nums[i], nums[NextNonZero]
                NextNonZero += 1
        