class Solution:
    def pivotInteger(self, n: int) -> int:
        arr = []
        x = 1
        flag = False
        for i in range(1,n+1):
            arr.append(i)
        for i in range(n):
            if sum(arr[0:x]) == sum(arr[x-1:n]):
                flag = True
                break
            x += 1
        
        if flag == False:
            return -1
        else:
            return x