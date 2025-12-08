VENV_PYTHON = .venv/bin/python
SRC = src tests


fix-code:
	@echo "Running code fixes..."
	$(VENV_PYTHON) -m black $(SRC) --line-length=120

	$(VENV_PYTHON) -m isort $(SRC)

	$(VENV_PYTHON) -m ruff check $(SRC) --line-length=120 --fix



pre-comit:
	@echo "Running pre-commit checks..."

	make fix-code