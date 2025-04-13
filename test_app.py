from app import bubble_sort
from app import classify_triangle

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

def test_equilateral():
    assert classify_triangle(3, 3, 3) == "Equilateral"

def test_isosceles_side12():
    assert classify_triangle(3, 3, 4) == "Isosceles"

def test_isosceles_side13():
    assert classify_triangle(3, 4, 3) == "Isosceles"

def test_isosceles_side23():
    assert classify_triangle(4, 3, 3) == "Isosceles"

def test_scalene():
    assert classify_triangle(3, 4, 5) == "Scalene"
