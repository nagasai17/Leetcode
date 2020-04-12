class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items=[]
        self.min=float('INF')

    def push(self, x: int) -> None:
        if(x<=self.min):
            
            self.items.append(self.min)
            self.min=x
        self.items.append(x)    

    def pop(self) -> None:
        if not self.items:
            pass
        else:
            t=self.items[-1]
            self.items.pop()
            if(t==self.min):
                self.min=self.items[-1]
                self.items.pop()

    def top(self) -> int:
        if not self.items:
            return -1
        else:
            return self.items[-1]
        

    def getMin(self) -> int:
        if not self.items:
            return -1
        else:
            return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
