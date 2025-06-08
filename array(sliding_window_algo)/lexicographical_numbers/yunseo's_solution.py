class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        arr = []
        for i in range(1, n+1):
            arr.append(str(i))
        
        arr.sort()

        for i in range(n):
            arr[i] = int(arr[i])

        return arr  