import subprocess
from collections.abc import Sequence


def run(args: Sequence[str], /) -> str:
    completed_process = subprocess.run(args, text=True, capture_output=True)
    output = completed_process.stdout or completed_process.stderr
    return output.strip()
