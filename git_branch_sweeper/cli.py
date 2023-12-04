from InquirerPy import inquirer, utils

from git_branch_sweeper.git import Git, GitInitializationError
from git_branch_sweeper.styles import DEFAULT_STYLE, GREEN, ORANGE_BOLD_UNDERLINE


def main() -> None:
    try:
        git = Git()
    except GitInitializationError as e:
        print(e)
        return

    print()
    selected_branches = inquirer.checkbox(
        message="Select branches to delete:",
        choices=git.branches,
        style=DEFAULT_STYLE,
        transformer=lambda result: f"{len(result)} branch{'es' if len(result) != 1 else ''} selected",
        instruction=f"(use [space] to select, or [a] to toggle all)\n  Current branch: {git.current_branch}",
        show_cursor=False,
        raise_keyboard_interrupt=False,
        mandatory=False,
        keybindings={"toggle-all": [{"key": "a"}]},
    ).execute()

    if not selected_branches:
        print("No branches deleted.")
        return

    utils.color_print([(ORANGE_BOLD_UNDERLINE, "\nBranches for deletion:")])
    for index, branch in enumerate(selected_branches, start=1):
        print(f"{index}. {branch}")

    print()
    branch_count = len(selected_branches)
    confirm = inquirer.confirm(
        message=f"Delete {f'these {branch_count} branches' if branch_count > 1 else f'this branch'}?",
        style=DEFAULT_STYLE,
        default=False,
        raise_keyboard_interrupt=False,
        mandatory=False,
    ).execute()

    if not confirm:
        print("No branches deleted.")
        return

    output = git.delete(selected_branches)
    print(f"\n{output}\n")
    utils.color_print([(GREEN, "All selected branches deleted. 🧹✨")])


if __name__ == "__main__":
    main()
