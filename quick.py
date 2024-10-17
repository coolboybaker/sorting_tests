import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Тесты
def test_quick_sort():
    assert quick_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
    assert quick_sort([]) == []
    assert quick_sort([1]) == [1]
    assert quick_sort([3, 2, 1]) == [1, 2, 3]
    
    # Тест на время
    start_time = time.time()
    quick_sort(list(range(1000, 0, -1)))  # Сортируем массив из 1000 элементов
    end_time = time.time()
    
    print("Quick Sort Passed in", end_time - start_time, "seconds")

test_quick_sort()
