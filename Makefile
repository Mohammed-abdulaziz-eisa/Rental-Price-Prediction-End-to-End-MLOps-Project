.PHONY: run install clean check runner
.DEFAULT_GOAL:= runner  

run: install 
	cd src; poetry run python3 runner.py

install: pyproject.toml
	poetry update
	poetry install

clean:
	rm -rf `find . -name "__pycache__"`
	rm -rf `find . -name ".DS_Store"`
	rm -rf .ruff_cache

check:
	#poetry run ruff src/
	poetry run flake8 src/

runner: check run clean 