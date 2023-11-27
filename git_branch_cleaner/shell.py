import subprocess


def run_command(command: str) -> str:
    output = subprocess.check_output(command, shell=True)
    return output.decode().strip()
