import subprocess

from InquirerPy import inquirer, utils


def main() -> None:
    style = utils.get_style(  # 48A8B5
        {
            "question": "bold",
            "answer": "#48A8B5",
            "pointer": "#48A8B5",
            # "questionmark": "#1AA963 bold",
            "questionmark": "orange bold",
            # "answermark": "#1AA963 bold",
            "answermark": "orange bold",
            # "checkbox": "#1AA963",
            # "answered_question": "#abb2bf",
            # "instruction": "#abb2bf",
        },
        style_override=False,
    )
    try:
        raw_results = (
            subprocess.check_output(
                "git branch '--format=%(refname:lstrip=2)'", shell=True
            )
            .decode()
            .rstrip()
        )
    except subprocess.CalledProcessError:
        return

    results = raw_results.split("\n")
    current_branches = [branch for branch in results if branch]

    print()
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
        print("No branches deleted.")
        return

    utils.color_print([("orange bold underline", "\nBranches for deletion:")])
    for index, branch in enumerate(branches, start=1):
        utils.color_print([("", f"{index}. {branch}")])

    print()
    branch_count = len(branches)
    confirm = inquirer.confirm(
        message=f"Delete {f'these {branch_count}' if branch_count > 1 else 'this'} branch{'es' if branch_count > 1 else ''}?",
        style=style,
        default=False,
        raise_keyboard_interrupt=False,
        mandatory=False,
    ).execute()

    if not confirm:
        print("No branches deleted.")
        return

    print()
    a = subprocess.check_output(
        f"git branch -D {' '.join(branches)}", shell=True
    ).decode()
    print(a)

    utils.color_print([("#1AAE65", "All selected branches deleted.")])


if __name__ == "__main__":
    main()
