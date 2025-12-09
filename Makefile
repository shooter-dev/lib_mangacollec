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