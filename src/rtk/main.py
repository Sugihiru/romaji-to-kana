from rtk.hiraganas import ROMANJI_TO_HIRAGANAS


def to_hiraganas(text: str) -> str:
    text = text.lower().strip()
    for consonant in "zrtpqsdfghjklmwxcvb":
        text = text.replace(consonant * 2, f"っ{consonant}")

    for romaji, hiragana in ROMANJI_TO_HIRAGANAS.items():
        text = text.replace(romaji, hiragana)
    return text.strip()
