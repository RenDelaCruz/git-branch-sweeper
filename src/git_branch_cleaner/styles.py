from typing import Final

from InquirerPy import InquirerPyStyle, utils

GREEN: Final[str] = "#1AAE65"
ORANGE_BOLD_UNDERLINE: Final[str] = "orange bold underline"

DEFAULT_STYLE: Final[InquirerPyStyle] = utils.get_style(
    {
        "question": "bold",
        "answer": "#48A8B5",
        "pointer": "#48A8B5",
        "questionmark": "orange bold",
        "answermark": "orange bold",
    },
    style_override=False,
)
