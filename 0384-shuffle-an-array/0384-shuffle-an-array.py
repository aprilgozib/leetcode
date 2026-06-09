class Solution:

    def __init__(self, nums: List[int]):
        # store og array
        self.orginal = nums[:] # self.orignal = nums -> nums change -> orignal change
        self.nums = nums

    def reset(self) -> List[int]:
        # return og array
        self.nums = self.orginal[:]
        return self.nums

    def shuffle(self) -> List[int]:
        # random shuffle
        # start at the back, swap with random rocation under curr
        for i in range(len(self.nums) - 1, 0, -1):
            j = random.randint(0, i)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()