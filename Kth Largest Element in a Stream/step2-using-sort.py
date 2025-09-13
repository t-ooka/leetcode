class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream = nums
        self.k = k
        

    def add(self, val: int) -> int:
        self.stream.append(val)
        self.stream.sort()
        return self.stream[len(self.stream) - self.k]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
