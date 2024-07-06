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
        self.default_branch = self.get_default_branch()

        if len(branches) == 2 and self.current_branch != self.default_branch:
            raise GitInitializationError(
                f"Only 1 other branch found. Cannot delete the default branch: {self.default_branch}"
            )

        merged_branches = self.get_branches(
            merged=True, base_branch=self.default_branch
        )

        self.merged_branches = [
            branch
            for branch in merged_branches
            if "*" not in branch and branch != self.default_branch
        ]
        self.unmerged_branches = [
            branch
            for branch in branches
            if "*" not in branch
            and branch != self.default_branch
            and branch not in self.merged_branches
        ]

    def is_in_git_repository(self) -> bool:
        output = process.run(["git", "rev-parse", "--is-inside-work-tree"])
        return output == "true"

    def get_branches(
        self, *, merged: bool | None = None, base_branch: str | None = None
    ) -> Sequence[str]:
        branch_command = ["git", "branch", "--format", "%(refname:short)%(HEAD)"]

        if merged is not None:
            merged_flag = "--merged" if merged else "--no-merged"
            branch_command.append(merged_flag)

            if base_branch:
                branch_command.append(base_branch)

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
