import pytest

from rtk.main import to_hiragana


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("aeiou", "あえいおう"),
        ("arigatou", "ありがとう"),
        ("sayonara", "さよなら"),
        ("furimukazu", "ふりむかず"),
        ("natte", "なって"),
        ("tamashii", "たましい"),
        ("satteshimau", "さってしまう"),
        ("genjitsu", "げんじつ"),
        ("kieteshimatta", "きえてしまった"),
        ("honnou", "ほんのう"),
        ("kyou", "きょう"),
        ("ryougashi", "りょうがし"),
    ],
)
def test_to_hiragana(test_input: str, expected: str):
    assert to_hiragana(test_input) == expected
