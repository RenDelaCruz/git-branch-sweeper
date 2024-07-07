[![python 3.10](https://img.shields.io/badge/Python-3.10-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![mypy: checked](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)

# git-branch-sweeper

🧹✨ Interactive CLI tool to delete multiple local Git branches at once.

![](https://raw.githubusercontent.com/RenDelaCruz/git-branch-sweeper/main/assets/example.svg)

<!--
https://carbon.now.sh/?bg=rgba%28255%2C255%2C255%2C1%29&t=vscode&wt=none&l=auto&width=710&ds=false&dsyoff=20px&dsblur=68px&wc=true&wa=false&pv=26px&ph=24px&ln=false&fl=1&fm=Hack&fs=14px&lh=133%25&si=false&es=1x&wm=false&code=%2524%2520git-branch-sweeper%250A%250A%253F%2520Select%2520branches%2520to%2520delete%253A%2520%28use%2520%255Bspace%255D%2520to%2520select%252C%2520or%2520%255Ba%255D%2520to%2520toggle%2520all%29%250A%2520%2520Current%2520branch%253A%2520PROJ-833%252Fchecked-out-branch%250A%250A%2520%2520%25E2%2595%25AD%25E2%2594%2580%25E2%2594%2580%2520Merged%2520into%2520master%2520%25E2%2594%2580%25E2%2594%2580%25E2%2595%25AE%250A%2520%2520%25E2%2597%2589%2520PROJ-654%252Fold-ticket%250A%2520%2520%25E2%2597%2589%2520PROJ-934%252Fextra-branch%250A%250A%2520%2520%25E2%2595%25AD%25E2%2594%2580%25E2%2594%2580%2520Not%2520merged%2520%25E2%2594%2580%25E2%2594%2580%25E2%2594%2580%25E2%2594%2580%25E2%2594%2580%25E2%2594%2580%25E2%2594%2580%25E2%2594%2580%25E2%2594%2580%25E2%2595%25AE%250A%25E2%259D%25AF%2520%25E2%2597%2589%2520PROJ-324%252Ftesting-feat%250A%2520%2520%25E2%2597%258B%2520PROJ-435%252Fcurrent-task%250A%250A%25E2%2586%25B5%250A%250A%2520%2520%25E2%2595%25AD%25E2%2594%2580%25E2%2594%2580%2520Branches%2520for%2520deletion%2520%25E2%2594%2580%25E2%2594%2580%25E2%2595%25AE%250A%2520%2520%25E2%2597%2589%2520PROJ-654%252Fold-ticket%250A%2520%2520%25E2%2597%2589%2520PROJ-934%252Fextra-branch%250A%2520%2520%25E2%2597%2589%2520PROJ-324%252Ftesting-feat%250A%250A%253F%2520Delete%2520these%25203%2520branches%253F%2520%28y%252FN%29%2520Yes%250A%250ADeleted%2520branch%2520PROJ-654%252Fold-ticket%2520%28was%2520cb0c590%29.%250ADeleted%2520branch%2520PROJ-934%252Fextra-branch%2520%28was%2520cb0c590%29.%250ADeleted%2520branch%2520PROJ-324%252Ftesting-feat%2520%28was%25202b2e997%29.%250A%250A%25E2%259C%25A8%25F0%259F%25A7%25B9%2520All%2520selected%2520branches%2520deleted.%2520%25F0%259F%25A7%25B9%25E2%259C%25A8
-->

<!-- ```sh
$ git-branch-sweeper

? Select branches to delete: (use [space] to select, or [a] to toggle all)
  Current branch: PROJ-833/checked-out-branch

  ╭── Merged into master ──╮
  ◉ PROJ-654/old-ticket
  ◉ PROJ-934/extra-branch

  ╭── Not merged ─────────╮
❯ ◉ PROJ-324/testing-feat
  ○ PROJ-435/current-task

↵

  ╭── Branches for deletion ──╮
  ◉ PROJ-654/old-ticket
  ◉ PROJ-934/extra-branch
  ◉ PROJ-324/testing-feat

? Delete these 3 branches? (y/N) Yes

Deleted branch PROJ-654/old-ticket (was cb0c590).
Deleted branch PROJ-934/extra-branch (was cb0c590).
Deleted branch PROJ-324/testing-feat (was 2b2e997).

✨🧹 All selected branches deleted. 🧹✨
``` -->


## Installation

```sh
pip install git-branch-sweeper
```

## Usage

```sh
git-branch-sweeper
```

or

```sh
git branch-sweeper
```
