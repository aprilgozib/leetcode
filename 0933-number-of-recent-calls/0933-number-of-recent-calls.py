class RecentCounter:

    def __init__(self):
        self.q1 = deque()

    def ping(self, t: int) -> int:
        self.q1.append(t)
        while self.q1[0] < t - 3000:
            self.q1.popleft()
        return len(self.q1) 


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)