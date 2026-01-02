def unplaced_fruits(fruits, baskets):
    n = len(fruits)
    used = [False] * n  
    unplaced_count = 0

    for fruit in fruits:
        placed = False
        for i in range(n):
            if not used[i] and baskets[i] >= fruit:
                used[i] = True
                placed = True
                break
        if not placed:
            unplaced_count += 1

    return unplaced_count