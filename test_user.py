from user import get_username

def test_get_username():
    assert get_username(1) == "tomas"
    assert get_username(3) == "vendulka"
    assert get_username(99) is None
