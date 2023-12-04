from collections.abc import Sequence

from git_branch_sweeper import shell


class GitInitializationError(Exception):
    pass


class Git:
    def __init__(self) -> None:
        if not self.is_in_git_repository:
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

    @property
    def is_in_git_repository(self) -> bool:
        result = shell.run_command("git rev-parse --is-inside-work-tree")
        return result == "true"

    def get_branches(self) -> Sequence[str]:
        result = shell.run_command("git branch --format '%(refname:short)%(HEAD)'")
        return result.split("\n") if result else []

    def delete(self, branches_to_delete: Sequence[str]) -> str:
        return shell.run_command(f"git branch -D {' '.join(branches_to_delete)}")
