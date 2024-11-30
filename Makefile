run: install 
	cd src; poetry run python3 runner.py

install: pyproject.toml
	poetry update
	poetry install

clean:
	rm -rf `find . -name "__pycache__"`
	rm -rf `find . -name ".DS_Store"`