from typing import Final

from InquirerPy import utils

BLUE: Final[str] = "#48A8B5"
GREEN: Final[str] = "#1BB266"
ORANGE_BOLD_UNDERLINE: Final[str] = "orange bold underline"

DEFAULT_STYLE: Final = utils.get_style(
    {
        "question": "bold",
        "answer": BLUE,
        "pointer": BLUE,
        "questionmark": "orange bold",
        "answermark": "orange bold",
    },
    style_override=False,
)
