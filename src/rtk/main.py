import argparse
import os
import pathlib
import random

from rtk.hiraganas import ROMANJI_TO_HIRAGANAS

MODE_WORD = "word"
MODE_LINE = "line"
POSSIBLE_DOUBLE_CONSONANT = "zrtpqsdfghjklmwxcvb"


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

    for romaji, hiragana in ROMANJI_TO_HIRAGANAS.items():
        text = text.replace(romaji, hiragana)
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
    args = parser.parse_args()
    elements = list(parse_files(pathlib.Path(args.source), args.mode))

    # Display elements and their answer
    random.shuffle(elements)
    elements_translated = {to_hiragana(x): x for x in elements}
    for hiragana, romaji in elements_translated.items():
        print(hiragana)
        input()
        print(romaji)
        print("--")


if __name__ == "__main__":
    main()
