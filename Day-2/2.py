# Binary Search (Lower Bound)

def lower_bound(prices, target):
    low = 0
    high = len(prices) - 1
    answer = -1

    while low <= high:
        mid = (low + high) // 2

        if prices[mid] >= target:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer


prices = [25000, 32000, 45000, 50000, 55000, 70000]

target = int(input("Enter target price: "))

index = lower_bound(prices, target)

if index != -1:
    print("First product price is", prices[index])
    print("Found at index", index)
else:
    print("No product found")