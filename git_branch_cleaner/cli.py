from InquirerPy import inquirer, utils

from git_branch_cleaner.git import Git
from git_branch_cleaner.styles import DEFAULT_STYLE, GREEN, ORANGE_BOLD_UNDERLINE


def main() -> None:
    git = Git()
    if not git.branches:
        print(
            f"Only 1 branch found. Cannot delete the current branch: {git.current_branch}"
        )
        return

    print()
    selected_branches = inquirer.checkbox(
        message="Select branches to delete:",
        choices=git.branches,
        style=DEFAULT_STYLE,
        transformer=lambda result: f"{len(result)} branch{'es' if len(result) != 1 else ''} selected",
        instruction=f"(use <space> to select)\n  Current branch: {git.current_branch}",
        show_cursor=False,
        raise_keyboard_interrupt=False,
        mandatory=False,
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
        message=f"Delete {f'these {branch_count}' if branch_count > 1 else 'this'} branch{'es' if branch_count > 1 else ''}?",
        style=DEFAULT_STYLE,
        default=False,
        raise_keyboard_interrupt=False,
        mandatory=False,
    ).execute()

    if not confirm:
        print("No branches deleted.")
        return

    output = git.delete(selected_branches)
    print(f"\n{output}")
    utils.color_print([(GREEN, "All selected branches deleted.")])


if __name__ == "__main__":
    main()
