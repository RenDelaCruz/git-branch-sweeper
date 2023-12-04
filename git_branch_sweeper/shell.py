import subprocess


def run_command(command: str) -> str:
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        output = e.output

    return output.decode().strip()
