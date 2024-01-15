
class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def zeroknapsack(items, capacity, currentIndex):
    if capacity <= 0 or currentIndex < 0 or currentIndex >= len(items):
        return 0
    elif items[currentIndex].weight <= capacity:
        profit1 = items[currentIndex].profit + zeroknapsack(items, capacity - items[currentIndex].weight, currentIndex + 1)
        profit2 = zeroknapsack(items, capacity, currentIndex + 1)
        return max(profit1, profit2)
    else:
        return zeroknapsack(items, capacity, currentIndex + 1)

mango = Item(34, 9)
grapes = Item(30, 5)
apple = Item(25, 7)
cheeku = Item(50, 3)

items = [mango, grapes, apple, cheeku]
print(zeroknapsack(items, 7, 0))


# Reduce less line of code

class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def zeroknapsack(items, capacity, currentIndex):
    if capacity <= 0 or currentIndex < 0 or currentIndex >= len(items):
        return 0

    if items[currentIndex].weight > capacity:
        return zeroknapsack(items, capacity, currentIndex + 1)

    return max(items[currentIndex].profit + zeroknapsack(items, capacity - items[currentIndex].weight, currentIndex + 1),
               zeroknapsack(items, capacity, currentIndex + 1))


mango = Item(34, 9)
grapes = Item(30, 5)
apple = Item(25, 7)
cheeku = Item(50, 3)

items = [mango, grapes, apple, cheeku]
print(zeroknapsack(items, 7, 0))

# Reduce in to less line of code


class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def zeroknapsack(items, capacity, currentIndex):
    if capacity <= 0 or currentIndex < 0 or currentIndex >= len(items):
        return 0

    return max(items[currentIndex].profit + zeroknapsack(items, capacity - items[currentIndex].weight, currentIndex + 1) if items[currentIndex].weight <= capacity else 0,
               zeroknapsack(items, capacity, currentIndex + 1))

mango = Item(34, 9)
grapes = Item(30, 5)
apple = Item(25, 7)
cheeku = Item(50, 3)

items = [mango, grapes, apple, cheeku]

print(zeroknapsack(items, 7, 0))
