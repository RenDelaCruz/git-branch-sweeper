import subprocess
import sys
from collections.abc import Sequence

from git_branch_cleaner import shell


class Git:
    def __init__(self) -> None:
        try:
            output = (
                subprocess.check_output(
                    "git branch --format '%(refname:short)%(HEAD)'", shell=True
                )
                .decode()
                .rstrip()
            )
        except subprocess.CalledProcessError:
            # Automatically outputs standard error to terminal
            sys.exit(0)

        result = output.split("\n")
        self.current_branch = next(
            branch for branch in result if "*" in branch
        ).removesuffix("*")
        self.branches: Sequence[str] = [
            branch for branch in result if branch and "*" not in branch
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
