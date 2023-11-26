import subprocess
import sys
from collections.abc import Sequence


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

    def delete(self, branches_to_delete: Sequence[str]) -> str:
        output = subprocess.check_output(
            f"git branch -D {' '.join(branches_to_delete)}", shell=True
        )
        return output.decode()
