from app import bubble_sort

def test_bubble_sort1():
    arr = []
    assert bubble_sort(arr) == []

def test_bubble_sort2():
    arr = [7]
    assert bubble_sort(arr) == [7]

def test_bubble_sort3():
    arr = [3, 7]
    assert bubble_sort(arr) == [3, 7]

def test_bubble_sort4():
    arr = [7, 3]
    assert bubble_sort(arr) == [3, 7]

def test_bubble_sort5():
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert bubble_sort(arr) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_bubble_sort6():
    arr = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
    assert bubble_sort(arr) == [-9, -8, -7, -6, -5, -4, -3, -2, -1]

def test_bubble_sort7():
    arr = [7, 7, 7, 7, 7, 7, 7, 7, 7]
    assert bubble_sort(arr) == [7, 7, 7, 7, 7, 7, 7, 7, 7]

def test_bubble_sort8():
    arr = [7, 7, 7, 7, 7, 3, 3, 3, 3, 3]
    assert bubble_sort(arr) == [3, 3, 3, 3, 3, 7, 7, 7, 7, 7]

def test_bubble_sort9():
    arr = [32767, 32766, -32768, -32767]
    assert bubble_sort(arr) == [-32768, -32767, 32766, 32767]

def test_bubble_sort10():
    arr = [2147483647, 2147483646, -2147483648, -2147483647]
    assert bubble_sort(arr) == [-2147483648, -2147483647, 2147483646, 2147483647]
