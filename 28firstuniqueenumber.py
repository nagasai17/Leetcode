class FirstUnique:

    def __init__(self, nums: List[int]):
        self.l={}
        self.nums=collections.deque()
        for num in nums:
            self.add(num)
        
        

    def showFirstUnique(self) -> int:
        if(not self.l):
            return -1
        
        while len(self.nums)>0 and self.nums[0] in self.l   and self.l[self.nums[0]]>1:
            self.nums.popleft()
           
        if(not self.nums):
            return -1
        else:
            return self.nums[0]
            

    def add(self, v: int) -> None:
        self.nums.append(v)
        if(v not in self.l):
              self.l[v]=1
        else:
              self.l[v]+=1
    


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
