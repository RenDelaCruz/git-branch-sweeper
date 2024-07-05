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

    def get_branches(self) -> Sequence[str]:
        output = process.run(["git", "branch", "--format", "%(refname:short)%(HEAD)"])
        return output.replace(" ", "").split("\n") if output else []

    def delete(self, branches_to_delete: Sequence[str]) -> str:
        return process.run(["git", "branch", "-D", *branches_to_delete])
