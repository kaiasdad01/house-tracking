.PHONY: install install-dev test lint format type-check clean run-api run-ui docs

# Python and pip
PYTHON := python3
PIP := pip

# Virtual environment
VENV := venv
VENV_BIN := $(VENV)/bin

# Source code directory
SRC_DIR := src/real_estate_tracker

# Installation commands
install:
	$(PIP) install -r requirements.txt

install-dev:
	$(PIP) install -r requirements-dev.txt
	$(VENV_BIN)/pre-commit install

# Testing
test:
	$(VENV_BIN)/pytest tests/ -v

test-cov:
	$(VENV_BIN)/pytest tests/ --cov=$(SRC_DIR) --cov-report=html --cov-report=term

test-unit:
	$(VENV_BIN)/pytest tests/unit/ -v

test-integration:
	$(VENV_BIN)/pytest tests/integration/ -v

# Code quality
lint:
	$(VENV_BIN)/flake8 $(SRC_DIR) tests/
	$(VENV_BIN)/mypy $(SRC_DIR)

format:
	$(VENV_BIN)/black $(SRC_DIR) tests/
	$(VENV_BIN)/isort $(SRC_DIR) tests/

format-check:
	$(VENV_BIN)/black --check $(SRC_DIR) tests/
	$(VENV_BIN)/isort --check-only $(SRC_DIR) tests/

type-check:
	$(VENV_BIN)/mypy $(SRC_DIR)

# Pre-commit
pre-commit:
	$(VENV_BIN)/pre-commit run --all-files

# Application commands
run-api:
	$(VENV_BIN)/uvicorn $(SRC_DIR).api.main:app --reload --host 0.0.0.0 --port 8000

run-ui:
	$(VENV_BIN)/streamlit run $(SRC_DIR)/ui/main.py --server.port 8501

run-scraper:
	$(VENV_BIN)/python -m $(SRC_DIR).data.scraper

# Database
db-migrate:
	$(VENV_BIN)/alembic upgrade head

db-downgrade:
	$(VENV_BIN)/alembic downgrade -1

db-revision:
	$(VENV_BIN)/alembic revision --autogenerate -m "$(MESSAGE)"

# dbt commands
dbt-deps:
	$(VENV_BIN)/dbt deps --project-dir dbt/

dbt-run:
	$(VENV_BIN)/dbt run --project-dir dbt/

dbt-test:
	$(VENV_BIN)/dbt test --project-dir dbt/

# Development setup
setup-dev: install-dev
	cp .env.example .env
	@echo "Please edit .env file with your configuration"

# Cleanup
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf build/
	rm -rf dist/
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/

# Docker commands
docker-build:
	docker build -t real-estate-tracker .

docker-run:
	docker run -p 8000:8000 -p 8501:8501 real-estate-tracker

# Documentation
docs:
	$(VENV_BIN)/sphinx-build -b html docs/ docs/_build/html

docs-serve:
	cd docs/_build/html && python -m http.server 8080

# Help
help:
	@echo "Available commands:"
	@echo "  install      - Install production dependencies"
	@echo "  install-dev  - Install development dependencies"
	@echo "  test         - Run all tests"
	@echo "  test-cov     - Run tests with coverage report"
	@echo "  lint         - Run linting checks"
	@echo "  format       - Format code with black and isort"
	@echo "  type-check   - Run mypy type checking"
	@echo "  run-api      - Start FastAPI server"
	@echo "  run-ui       - Start Streamlit UI"
	@echo "  setup-dev    - Set up development environment"
	@echo "  clean        - Clean up temporary files"