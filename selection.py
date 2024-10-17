import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Тесты
def test_selection_sort():
    assert selection_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
    assert selection_sort([]) == []
    assert selection_sort([1]) == [1]
    assert selection_sort([3, 2, 1]) == [1, 2, 3]
    
    # Тест на время
    start_time = time.time()
    selection_sort(list(range(1000, 0, -1)))  # Сортируем массив из 1000 элементов
    end_time = time.time()
    
    print("Selection Sort Passed in", end_time - start_time, "seconds")

test_selection_sort()
