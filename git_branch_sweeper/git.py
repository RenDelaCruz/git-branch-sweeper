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
        self.default_branch = self.get_default_branch()

    @property
    def is_in_git_repository(self) -> bool:
        result = shell.run_command("git rev-parse --is-inside-work-tree")
        return result == "true"

    def get_branches(self, *, merged: bool | None = None) -> Sequence[str]:
        if merged is not None:
            extra = "--merged" if merged else "--no-merged"
        else:
            extra = ""

        branches = shell.run_command(
            f"git branch --format '%(refname:short)%(HEAD)' {extra}"
        )
        return branches.split("\n") if branches else []

    def get_default_branch(self) -> str:
        remote = shell.run_command("git remote show")
        return shell.run_command(
            f"basename $(git symbolic-ref --short refs/remotes/{remote}/HEAD)"
        )

    def delete(self, branches_to_delete: Sequence[str]) -> str:
        return shell.run_command(f"git branch -D {' '.join(branches_to_delete)}")
