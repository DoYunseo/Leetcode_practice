class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.forward_history = [homepage]
        self.backward_history = []

    def visit(self, url: str) -> None:
        self.forward_history.append(url)
        self.backward_history = []
        

    def back(self, steps: int) -> str:
        for i in range(steps):
            if len(self.forward_history) > 1:
                top_link = self.forward_history.pop()
                self.backward_history.append(top_link)
        if len(self.forward_history) > 0:
            return self.forward_history[-1]
        

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if len(self.backward_history) > 0:
                top_link = self.backward_history.pop()
                self.forward_history.append(top_link)
        if len(self.forward_history) > 0:
            return self.forward_history[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)