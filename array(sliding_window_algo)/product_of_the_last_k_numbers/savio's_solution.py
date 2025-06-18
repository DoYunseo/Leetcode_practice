class ProductOfNumbers:

    def __init__(self):
        self.res = []
        

    def add(self, num: int) -> None:
        if num == 0:
            self.res = []
        else:
            if len(self.res) == 0:
                self.res.append(num)
            else:
                self.res.append(self.res[-1] * num)
        
        

    def getProduct(self, k: int) -> int:
        if k == len(self.res):
            return self.res[-1]
        elif k > len(self.res):
            return 0
        else:
            return self.res[-1] // self.res[-k-1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)