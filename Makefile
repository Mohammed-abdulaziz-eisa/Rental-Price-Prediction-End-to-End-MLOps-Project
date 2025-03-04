.PHONY: run_builder install clean check run_builder run_inference
.DEFAULT_GOAL:= run_inference  

run_builder: install 
	cd src; poetry run python3 runner_builder.py

run_inference: install
	cd src; poetry run python3 runner_inference.py

install: pyproject.toml
	poetry update
	poetry install

clean:
	rm -rf `find . -name "__pycache__"`
	rm -rf `find . -name ".DS_Store"`
	rm -rf .ruff_cache

check:
	#poetry run ruff src/
	#poetry run flake8 src/

runner_builder: check run_builder clean 

runner_inference: check run_inference clean 