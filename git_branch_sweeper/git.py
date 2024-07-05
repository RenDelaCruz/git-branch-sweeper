from collections.abc import Sequence

from git_branch_sweeper import process


class GitInitializationError(Exception):
    pass


class Git:
    def __init__(self) -> None:
        if not self.is_in_git_repository():
            raise GitInitializationError("Not in a Git repository.")

        branches = self.get_branches()
        if not branches:
            raise GitInitializationError("No branches found.")

        if len(branches) == 1:
            current_branch = branches[0].removesuffix("*")
            raise GitInitializationError(
                f"Only 1 branch found. Cannot delete the current branch: {current_branch}"
            )

        self.current_branch = next(
            branch for branch in branches if "*" in branch
        ).removesuffix("*")
        self.branches: Sequence[str] = [
            branch for branch in branches if branch and "*" not in branch
        ]

    def is_in_git_repository(self) -> bool:
        output = process.run(["git", "rev-parse", "--is-inside-work-tree"])
        return output == "true"

    def get_branches(self, *, merged: bool | None = None) -> Sequence[str]:
        branch_command = ["git", "branch", "--format", "%(refname:short)%(HEAD)"]
        if merged is not None:
            merged_flag = "--merged" if merged else "--no-merged"
            branch_command.append(merged_flag)

        output = process.run(branch_command)
        return output.replace(" ", "").split("\n") if output else []

    def get_default_branch(self) -> str:
        remote = process.run(["git", "remote", "show"])
        output = process.run(
            ["git", "symbolic-ref", "--short", f"refs/remotes/{remote}/HEAD"]
        )
        return output.removeprefix(f"{remote}/")

    def delete(self, branches_to_delete: Sequence[str]) -> str:
        return process.run(["git", "branch", "-D", *branches_to_delete])
