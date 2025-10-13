class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink = 0
        full = numBottles
        empty = 0
        
        while (full != 0):
            #1. Drink
            drink += full  
            empty = full + empty 
            #2. Exchange
            full = empty // numExchange
            empty = empty % numExchange 
            numBottles = full + empty 
            
        return drink