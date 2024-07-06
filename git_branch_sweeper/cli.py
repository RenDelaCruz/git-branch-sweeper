from InquirerPy import inquirer, utils
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

from git_branch_sweeper.git import Git, GitInitializationError
from git_branch_sweeper.styles import BOLD, DEFAULT_STYLE, ORANGE
from git_branch_sweeper.utils import get_fieldset_heading, get_max_length_in_sequence


def main() -> None:
    try:
        git = Git()
    except GitInitializationError as e:
        print(e)
        return

    choices: list[Choice | Separator] = []
    for branches, title, enabled in (
        (git.merged_branches, f"Merged into {git.default_branch}", True),
        (git.unmerged_branches, "Not merged", False),
    ):
        if not branches:
            continue

        max_branch_length = get_max_length_in_sequence(branches)
        heading = get_fieldset_heading(title=title, min_length=max_branch_length)
        choices.extend(
            [
                Separator(""),
                Separator(heading),
                *[Choice(branch, enabled=enabled) for branch in branches],
            ]
        )

    print()
    selected_branches = inquirer.checkbox(
        message="Select branches to delete:",
        choices=choices,
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

    max_branch_length = get_max_length_in_sequence(selected_branches)
    branches_for_deletion_heading = get_fieldset_heading(
        title="Branches for deletion", min_length=max_branch_length
    )
    utils.color_print([(ORANGE, f"\n  {branches_for_deletion_heading}")])
    for branch in selected_branches:
        utils.color_print([(ORANGE, "  ◉ "), ("", branch)])

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
    utils.color_print([(BOLD, "✨🧹 All selected branches deleted. 🧹✨")])


if __name__ == "__main__":
    main()
