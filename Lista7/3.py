# quicksort.py
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


# mergesort.py
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# binary_search.py
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# linear_search.py
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Przykład użycia algorytmów sortowania
arr = [5, 3, 8, 2, 1, 9, 4]
sorted_arr = quicksort(arr)
print("Posortowana lista (quicksort):", sorted_arr)  # [1, 2, 3, 4, 5, 8, 9]

arr = [5, 3, 8, 2, 1, 9, 4]
sorted_arr = mergesort(arr)
print("Posortowana lista (mergesort):", sorted_arr)  # [1, 2, 3, 4, 5, 8, 9]

# Przykład użycia algorytmów wyszukiwania
arr = [1, 2, 3, 4, 5, 8, 9]
target = 3
index = binary_search(arr, target)
if index != -1:
    print(f"Liczba {target} znaleziona na indeksie {index}")
else:
    print(f"Liczba {target} nie znaleziona")

target = 6
index = linear_search(arr, target)
if index != -1:
    print(f"Liczba {target} znaleziona na indeksie {index}")
else:
    print(f"Liczba {target} nie znaleziona")