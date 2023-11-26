[![python 3.10](https://img.shields.io/badge/Python-3.10-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![mypy: checked](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)

# git-branch-cleaner

🧹✨ Interactive CLI tool to delete multiple local git branches at once.

```sh
❯ git-branch-cleaner

? Select branches to delete: (use [space] to select, or [a] to toggle all)
  Current branch: PROJ-435_current-task 
  ◉ PROJ-654_old-ticket
❯ ◉ PROJ-934_extra-branch 
  ○ main

Branches for deletion:
1. PROJ-654_old-ticket 
2. PROJ-934_extra-branch 

? Delete these 2 branches? (y/N) Yes

Deleted branch PROJ-654_old-ticket (was cb0c590).
Deleted branch PROJ-934_extra-branch (was cb0c590).

All selected branches deleted.
```


## Installation

```sh
pip install git+https://github.com/RenDelaCruz/git-branch-cleaner.git
```

## Usage

```sh
git-branch-cleaner
```

or

```sh
git branch-cleaner
```
