.PHONY: format lint typecheck test check all

## Formate le code avec Black
format:
	poetry run black src/mangacollec_api/

## Lint le code avec Flake8
lint:
	poetry run flake8 src/mangacollec_api/

## Vérifie les types avec mypy
typecheck:
	poetry run mypy src/mangacollec_api/

## Lance les tests avec pytest
test:
	poetry run pytest -v --maxfail=5 --disable-warnings

## Vérifie tout (format, lint, typecheck, test)
check: format lint typecheck test

## Par défaut : check tout
all: check
