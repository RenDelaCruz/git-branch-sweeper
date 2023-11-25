import subprocess

from InquirerPy import inquirer, utils


def main() -> None:
    print()
    style = utils.get_style(  # 48A8B5
        {
            "question": "bold",
            "answer": "#48A8B5",
            "pointer": "#48A8B5",
            # "questionmark": "#1AA963 bold",
            # "questionmark": "orange bold",
            # "answermark": "#1AA963 bold",
            # "answermark": "orange bold",
            # "checkbox": "#1AA963",
            # "answered_question": "#abb2bf",
            # "instruction": "#abb2bf",
        },
        style_override=False,
    )
    raw_results = (
        subprocess.check_output("git branch '--format=%(refname:lstrip=2)'", shell=True)
        .decode()
        .rstrip()
        .split("\n")
    )
    current_branches = [branch for branch in raw_results if branch]

    branches = inquirer.checkbox(
        message="Select branches to delete:",
        choices=current_branches,
        # choices=[
        #     "TICKET-100_this-ticket",
        #     "TICKET-454_this-ticket",
        #     "TICKET-4230_this-ticket",
        #     "TICKET-1544_this-ticket",
        #     "TICKET-1234_this-ticket",
        #     "TICKET-1324_this-ticket",
        # ],
        style=style,
        # enabled_symbol="⬢",
        # enabled_symbol="💣",
        # disabled_symbol=" ",
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

    if not branches:
        return

    branch_count = len(branches)
    confirm = inquirer.confirm(
        message=f"Delete {f'these {branch_count}' if branch_count > 1 else 'this'} branch{'es' if branch_count > 1 else ''}?",
        style=style,
        default=False,
    ).execute()

    if confirm:
        print(branches)
        print("Selected branches deleted.")
    else:
        print("No branches deleted.")


if __name__ == "__main__":
    main()
