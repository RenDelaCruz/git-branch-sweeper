include .makefile.inc

ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
$(eval $(ARGS):;@:)

.PHONY: start
start: ## Executes the command-line interface
	poetry run python3 -m git_branch_sweeper.cli

.PHONY: publish
publish: ## Build and publish the project to PyPI
	poetry publish --build

.PHONY: shell
shell: ## Start an IPython shell for manual testing
	poetry run python3 -m IPython

## Code Analysis

.PHONY: format
format: ## Run black to format
	pre-commit run -a black

.PHONY: lint
lint: ## Run flake8 to lint
	pre-commit run -a flake8

.PHONY: sort
sort: ## Run isort to sort imports
	pre-commit run -a isort

.PHONY: type-check
type-check: ## Run mypy to type check
	pre-commit run -a mypy

## Dependencies

.PHONY: install
install: ## Adds dependency using poetry. Usage: make install (<package> | <package>@<version>) [dev]
ifeq ($(word 2, $(MAKECMDGOALS)),)
	@echo "Package name is required. Usage: make install (<package> | <package>@<version>) [dev]"
else
	poetry add $(word 2, $(MAKECMDGOALS)) $(if $(filter dev, $(word 3, $(MAKECMDGOALS))),--group dev)
endif

.PHONY: uninstall
uninstall: ## Removes dependency using poetry. Usage: make uninstall <package>
ifeq ($(word 2, $(MAKECMDGOALS)),)
	@echo "Package name is required. Usage: make uninstall <package>"
else
	poetry remove $(word 2, $(MAKECMDGOALS))
endif
