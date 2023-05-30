from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], -1, "test") == "test"
    assert arrs.get([5, 8, 4, 6], 3, "test") == 6
    assert arrs.get([5, 8, 4, 6], 1, "test") == 8


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3], -1, 1) == []
    assert arrs.my_slice([1, 2, 3], -1, -1) == []
    assert arrs.my_slice([1, 2, 3, 4], 1, 2) == [2]
    assert arrs.my_slice([1, 2, 3, 4], -2) == [3, 4]
    assert arrs.my_slice([1, 2, 8, 6, 9], 0, -2) == [1, 2, 8]
    assert arrs.my_slice([], 0, -2) == []
    assert arrs.my_slice([1, 2, 3, 4, 5], -6,) == [1, 2, 3, 4, 5]

