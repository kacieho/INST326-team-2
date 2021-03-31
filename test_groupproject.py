from groupproject import point

def test_point():
    assert point("fruit") == 5
    assert point("Animal") == 6
    assert point("WEATHER") == 7
    assert point("hi") == 2
    assert point("hello") == 5
    assert point("hellohellohell") == 14
    assert point("hellohellohello") == 15
    