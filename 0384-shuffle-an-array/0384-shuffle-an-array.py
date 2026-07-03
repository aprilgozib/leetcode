class Solution:

    def __init__(self, nums: List[int]):
        self.og = nums[:]
        self.nums = nums

    def reset(self) -> List[int]:
        # return og
        self.nums = self.og[:]
        return self.nums

    def shuffle(self) -> List[int]:
        # randon shuffle
        # back to front
        for i in range(len(self.nums) - 1, 0, -1):
            j = random.randint(0, i)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()