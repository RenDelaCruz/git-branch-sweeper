from collections.abc import Collection, Sequence
from typing import Final, TypeVar

T = TypeVar("T", bound=Collection[object])

PADDING: Final[int] = 2


def get_max_length_in_sequence(sequence: Sequence[T]) -> int:
    longest_item = max(sequence, key=len)
    return len(longest_item)


def get_fieldset_heading(title: str, min_length: int) -> str:
    if title:
        title = f" {title} "

    fill_length = max(0, min_length - len(title) - PADDING)
    return f"╭──{title}{'─' * fill_length}──╮"
