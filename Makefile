.PHONY: fix-code tests pre-comit

VENV_PYTHON = .venv/bin/python
SRC = src tests

fix-code:
	@echo "Running code fixes..."
	$(VENV_PYTHON) -m black $(SRC) --line-length=120

	$(VENV_PYTHON) -m isort $(SRC)

	$(VENV_PYTHON) -m ruff check $(SRC) --line-length=120 --fix

tests-code:
	@echo "Checking code..."
	$(VENV_PYTHON) -m black --check $(SRC) --line-length=120

	$(VENV_PYTHON) -m isort --check-only $(SRC)

	$(VENV_PYTHON) -m ruff check $(SRC) --line-length=120

tests:
	@echo "Running tests..."
	$(VENV_PYTHON) -m pytest tests


pre-comit:
	@echo "Running pre-commit checks..."

	make fix-code

	make tests-code

	make tests

increment-version:
	@echo "Incrementing version..."
	@CURRENT_VERSION=$$(grep 'version = ' pyproject.toml | head -n1 | sed 's/.*"\(.*\)".*/\1/'); \
	echo "Current version: $$CURRENT_VERSION"; \
	MAJOR=$$(echo $$CURRENT_VERSION | cut -d. -f1); \
	MINOR=$$(echo $$CURRENT_VERSION | cut -d. -f2); \
	PATCH=$$(echo $$CURRENT_VERSION | cut -d. -f3); \
	PATCH=$$((PATCH + 1)); \
	NEW_VERSION="$$MAJOR.$$MINOR.$$PATCH"; \
	echo "New version: $$NEW_VERSION"; \
	sed -i.bak "s/version = \"$$CURRENT_VERSION\"/version = \"$$NEW_VERSION\"/" pyproject.toml; \
	rm -f pyproject.toml.bak; \
	git add pyproject.toml; \
	echo "✅ Version updated to $$NEW_VERSION"