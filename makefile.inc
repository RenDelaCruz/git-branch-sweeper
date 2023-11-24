# Available colors
RED    := $(shell tput -Txterm setaf 1)
GREEN  := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
BLUE   := $(shell tput -Txterm setaf 6)
WHITE  := $(shell tput -Txterm setaf 7)
RESET  := $(shell tput -Txterm sgr0)

TARGET_MAX_CHAR_NUM=25

define HELP_SCRIPT
  use warnings;
  if (/^([A-Za-z0-9_-]+[%]?)*:(?:.*## (.*))?/) {
    if ($$2) { printf "${YELLOW}%-${TARGET_MAX_CHAR_NUM}s${GREEN}%s${RESET}\n", $$1, $$2 } 
    else { printf "${YELLOW}%-${TARGET_MAX_CHAR_NUM}s${RED}%s${RESET}\n", $$1, '<Missing Description>' }
  }
  if (/^## (.*)?/) { printf "\n${BLUE}[%s]${RESET}\n", $$1 }
endef
export HELP_SCRIPT

define SHOW_IDENTITY
  @[ -f ./.makefile.identity.inc ] && cat ./.makefile.identity.inc; echo '' || echo ''
endef

help: ## This menu
	${SHOW_IDENTITY}
	@echo 'Usage:'
	@echo '${YELLOW}make${RESET} ${GREEN}<target>${RESET}'
	@echo ''
	@echo 'Targets:'
	@perl -ne "$${HELP_SCRIPT}" $(MAKEFILE_LIST)
