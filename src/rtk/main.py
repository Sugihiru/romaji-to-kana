import argparse
import enum
import os
import pathlib
import random
from typing import Callable

from rtk.hiraganas import ROMAJI_TO_HIRAGANAS
from rtk.katakanas import ROMAJI_TO_KATAKANAS

MODE_WORD = "word"
MODE_LINE = "line"


class Alphabet(str, enum.Enum):
    HIRAGANA = "hiragana"
    KATAKANA = "katakana"
    RANDOM = "random"


POSSIBLE_DOUBLE_CONSONANT = "zrtpqsdfghjklmwxcvb"
POSSIBLE_DOUBLE_VOWELS = "aeuio"


def dir_path(filepath: str):
    if os.path.isdir(filepath):
        return filepath
    else:
        raise NotADirectoryError(filepath)


def to_hiragana(text: str) -> str:
    """Converts a romaji text to hiragana

    Args:
        text (str): Romaji text

    Returns:
        str: Hiragana text
    """
    text = text.lower().strip()

    # Manage sokuon for words like katta -> かった
    for consonant in POSSIBLE_DOUBLE_CONSONANT:
        text = text.replace(consonant * 2, f"っ{consonant}")

    for romaji, hiragana in ROMAJI_TO_HIRAGANAS.items():
        text = text.replace(romaji, hiragana)
    return text.strip()


def to_katakana(text: str) -> str:
    """Converts a romaji text to katakana

    Args:
        text (str): Romaji text

    Returns:
        str: KLatakana text
    """
    text = text.lower().strip()

    # Manage sokuon for words like Cup -> カップ
    for consonant in POSSIBLE_DOUBLE_CONSONANT:
        text = text.replace(consonant * 2, f"ッ{consonant}")

    # Manage double vowels for words like Case -> ケース
    for vowel in POSSIBLE_DOUBLE_VOWELS:
        text = text.replace(vowel * 2, f"{vowel}ー")

    for romaji, katakana in ROMAJI_TO_KATAKANAS.items():
        text = text.replace(romaji, katakana)
    return text.strip()


def parse_file(filepath: pathlib.Path, mode: str) -> set[str]:
    content = open(filepath, "r").read()
    if mode == MODE_WORD:
        return set(content.split())
    return set(content.split("\n"))


def parse_files(folder_path: pathlib.Path, mode: str) -> set[str]:
    elems: set[str] = set()
    for filepath in folder_path.rglob("*.txt"):
        elems |= parse_file(filepath, mode)
    # Clean and remove empty strings
    return {x.strip() for x in elems if x.strip()}


def get_kana_translator(alphabet: Alphabet) -> Callable:
    """Get the kana translator function corresponding to the chosen alphabet

    Args:
        alphabet (Alphabet): choice of alphabet

    Returns:
        Callable: translator function
    """
    if alphabet == Alphabet.HIRAGANA:
        return to_hiragana
    elif alphabet == Alphabet.KATAKANA:
        return to_katakana
    return random.choice((to_hiragana, to_katakana))


def main():
    parser = argparse.ArgumentParser(prog="rtk")
    parser.add_argument(
        "-s",
        "--source",
        type=dir_path,
        required=True,
        help="path to the folder containing the romaji texts",
    )
    parser.add_argument(
        "--mode",
        choices=[MODE_WORD, MODE_LINE],
        default=MODE_WORD,
        help="whether to display words or lines",
    )
    parser.add_argument(
        "--alphabet",
        choices=[
            Alphabet.HIRAGANA.name.lower(),
            Alphabet.KATAKANA.name.lower(),
            Alphabet.RANDOM.name.lower(),
        ],
        default=Alphabet.RANDOM,
        help="specific alphabet to use",
    )
    args = parser.parse_args()
    elements = list(parse_files(pathlib.Path(args.source), args.mode))

    # Display elements and their answer
    random.shuffle(elements)
    elements_translated = {get_kana_translator(args.alphabet)(x): x for x in elements}
    for hiragana, romaji in elements_translated.items():
        print(hiragana)
        input()
        print(romaji)
        print("--")


if __name__ == "__main__":
    main()
