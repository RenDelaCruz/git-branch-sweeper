include .makefile.inc

ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
$(eval $(ARGS):;@:)

## Dependencies

.PHONY: install
install: ## Adds dependency using poetry. Usage: make install <package>@<version> [dev]
ifeq ($(word 2, $(MAKECMDGOALS)),)
	@echo "Package name is required. Usage: make install <package>@<version> [dev]"
else ifeq ($(findstring @, $(word 2, $(MAKECMDGOALS))),)
	@echo "Version number is required. Usage: make install <package>@<version> [dev]"
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
