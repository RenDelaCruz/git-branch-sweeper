from typing import Final

from InquirerPy import utils

BLUE: Final[str] = "#48a8b5"
GREEN: Final[str] = "#98c379"
ORANGE: Final[str] = "orange"
BOLD: Final[str] = "bold"

DEFAULT_STYLE: Final = utils.get_style(
    {
        "question": BOLD,
        "answer": BLUE,
        "pointer": BLUE,
        "questionmark": " ".join([ORANGE, BOLD]),
        "answermark": " ".join([ORANGE, BOLD]),
        "separator": GREEN,
    },
    style_override=False,
)
