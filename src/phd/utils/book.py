from pathlib import Path

import phd

BOOK_MODULE_NAME: str = "book"
CHAPTERS_MODULE_NAME: str = "chapters"


def get_book_root() -> Path:
    return Path(phd.__file__).parent.parent / BOOK_MODULE_NAME


def get_chapters_root() -> Path:
    return get_book_root() / CHAPTERS_MODULE_NAME
