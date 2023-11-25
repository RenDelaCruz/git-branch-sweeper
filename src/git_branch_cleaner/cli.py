from InquirerPy import inquirer
from InquirerPy.utils import get_style


def main() -> None:
    style = get_style(
        {
            "question": "bold",
            # "answered_question": "#abb2bf",
            # "instruction": "#abb2bf",
        },
        style_override=False,
    )
    branches = inquirer.checkbox(
        message="Select branches to delete:",
        choices=[
            "TICKET-100_this-ticket",
            "TICKET-454_this-ticket",
            "TICKET-4230_this-ticket",
            "TICKET-1544_this-ticket",
            "TICKET-1234_this-ticket",
            "TICKET-1324_this-ticket",
        ],
        style=style,
        # enabled_symbol="⬢",
        # enabled_symbol="💣",
        # disabled_symbol="  ",
        # disabled_symbol="◯",
        # qmark="[?]",
        # amark=" ? ",
        transformer=lambda result: f"{len(result)} branch{'es' if len(result) != 1 else ''} selected",
        instruction="(use <space> to select)",
        # border=True,
        show_cursor=False,
        raise_keyboard_interrupt=False,
        mandatory=False,
    ).execute()

    if branches:
        print(branches)


if __name__ == "__main__":
    main()
