from collections import defaultdict
import heapq
from typing import List


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = foods
        self.cuisines = cuisines
        self.ratings = ratings
        self.map_food_to_cuisine = defaultdict(str)
        self.map_food_to_rating = defaultdict(int)
        self.cuisines_to_heap = defaultdict(list)

        for idx, cuisine in enumerate(self.cuisines):
            self.map_food_to_cuisine[self.foods[idx]] = cuisine
            self.map_food_to_rating[self.foods[idx]] = self.ratings[idx]
            heapq.heappush(
                self.cuisines_to_heap[cuisine], (-self.ratings[idx], self.foods[idx])
            )

    def changeRating(self, food: str, newRating: int) -> None:
        self.map_food_to_rating[food] = newRating
        cuisine = self.map_food_to_cuisine[food]
        heapq.heappush(self.cuisines_to_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisines_to_heap[cuisine]
        while heap:
            rating, food = heap[0]

            if -rating == self.map_food_to_rating[food]:
                return food

            heapq.heappop(heap)


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
