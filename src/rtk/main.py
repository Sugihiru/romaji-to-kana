from rtk.hiraganas import ROMANJI_TO_HIRAGANAS


def to_hiragana(text: str) -> str:
    """Converts a romaji text to hiragana

    Args:
        text (str): Romaji text

    Returns:
        str: Hiragana text
    """
    text = text.lower().strip()
    for consonant in "zrtpqsdfghjklmwxcvb":
        text = text.replace(consonant * 2, f"っ{consonant}")

    for romaji, hiragana in ROMANJI_TO_HIRAGANAS.items():
        text = text.replace(romaji, hiragana)
    return text.strip()
