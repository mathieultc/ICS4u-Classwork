import evaluation_prep


#test example1
def test_add():
    assert evaluation_prep.add(3, 6) == 9
    assert evaluation_prep.add(0, 0) == 0


#test example2
def test_sum_list():
    assert evaluation_prep.sum_list([1, 2, 3]) == 6
    assert evaluation_prep.sum_list([0, 0, 0]) == 0


#test example3
def test_word_count():
    assert evaluation_prep.word_count(["word", "hello", "word"]) == {"word": 2, "hello": 1}
    