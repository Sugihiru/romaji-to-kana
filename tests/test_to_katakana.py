import pytest

from rtk.main import to_katakana


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("keesu", "ケース"),
        ("kyarakutaa", "キャラクター"),
        ("koohii", "コーヒー"),
        ("eakon", "エアコン"),
        ("rajio", "ラジオ"),
        ("arubaito", "アルバイト"),
        ("toire", "トイレ"),
        ("raion", "ライオン"),
        ("terebi", "テレビ"),
        ("aisukuriimu", "アイスクリーム"),
    ],
)
def test_to_katakana(test_input: str, expected: str):
    assert to_katakana(test_input) == expected
