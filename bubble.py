import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Тесты
def test_bubble_sort():
    assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    
    # Тест на время
    start_time = time.time()
    bubble_sort(list(range(1000, 0, -1)))  # Сортируем массив из 1000 элементов
    end_time = time.time()
    
    print("Bubble Sort Passed in", end_time - start_time, "seconds")

test_bubble_sort()
