from list_function import insert_at, insert


def test_insert_at():
    original = [1, 2, 3, 4]
    expected = [1, 2, 5, 3, 4]
    result = insert_at(original, 5, 2)
    assert result == expected


def test_insert():
    original = [1, 2, 5, 6]
    expected = [1, 2, 3, 5, 6]
    result = insert(original, 3)
    assert result == expected

'''
def test_remove():
    original = [1, 2, 3, 4]
    expected = [1, 3, 4]
    result = remove_at(original, 1)
    assert result == expected
'''


  