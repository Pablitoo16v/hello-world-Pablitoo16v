from main import get_hi_message


def test_hi_message():
    message = get_hi_message()
    assert len(message) > 4
    assert message.startswith("Hi, ")
