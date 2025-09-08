# Contributing to Real Estate Tracker

First off, thank you for considering contributing to Real Estate Tracker! It's people like you that make this project a great tool for home buyers everywhere.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* **Use a clear and descriptive title**
* **Describe the exact steps to reproduce the problem**
* **Provide specific examples to demonstrate the steps**
* **Describe the behavior you observed and what behavior you expected**
* **Include screenshots if applicable**
* **Include your environment details** (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

* **Use a clear and descriptive title**
* **Provide a step-by-step description of the suggested enhancement**
* **Provide specific examples to demonstrate the enhancement**
* **Describe the current behavior and explain the expected behavior**
* **Explain why this enhancement would be useful**

### Pull Requests

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. If you've changed APIs, update the documentation
4. Ensure the test suite passes
5. Make sure your code lints
6. Issue that pull request!

## Development Process

### Setting up your development environment

1. **Fork and clone the repository:**
   ```bash
   git clone https://github.com/your-username/real-estate-tracker.git
   cd real-estate-tracker
   ```

2. **Set up virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

3. **Install development dependencies:**
   ```bash
   make install-dev
   ```

4. **Set up pre-commit hooks:**
   ```bash
   pre-commit install
   ```

5. **Copy environment configuration:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

### Making Changes

1. **Create a branch:**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

2. **Make your changes following our coding standards:**
   - Follow PEP 8 style guide
   - Use type hints
   - Write docstrings for functions and classes
   - Keep functions small and focused

3. **Run tests:**
   ```bash
   make test
   ```

4. **Run code quality checks:**
   ```bash
   make lint
   make format
   make type-check
   ```

5. **Commit your changes:**
   ```bash
   git add .
   git commit -m "feat: add new feature" # Use conventional commits
   ```

### Commit Message Convention

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

- `feat:` A new feature
- `fix:` A bug fix
- `docs:` Documentation only changes
- `style:` Changes that do not affect the meaning of the code
- `refactor:` A code change that neither fixes a bug nor adds a feature
- `test:` Adding missing tests or correcting existing tests
- `chore:` Changes to the build process or auxiliary tools

### Testing Guidelines

- Write tests for new features and bug fixes
- Maintain or improve code coverage
- Use descriptive test names
- Follow the AAA pattern (Arrange, Act, Assert)

### Code Style

We use several tools to maintain code quality:

- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting
- **mypy**: Type checking

These are automatically run by pre-commit hooks, but you can also run them manually:

```bash
make format  # Run black and isort
make lint    # Run flake8 and mypy
```

### Documentation

- Update docstrings for any new or modified functions
- Update the README.md if you change functionality
- Add or update type hints
- Update API documentation if you modify endpoints

### Project Structure

```
src/real_estate_tracker/
├── api/            # FastAPI routes and dependencies
├── data/           # Data collection and processing
├── models/         # Pydantic models and database schemas
├── services/       # Business logic
└── ui/             # Streamlit interface

tests/
├── unit/           # Unit tests
├── integration/    # Integration tests
└── fixtures/       # Test fixtures and utilities
```

## Python Style Guide

### General Principles
- Follow PEP 8
- Use meaningful variable and function names
- Keep functions small (ideally < 20 lines)
- Use type hints consistently
- Write docstrings for public functions and classes

### Example Code Style

```python
from typing import List, Optional
import logging

logger = logging.getLogger(__name__)

class PropertyAnalyzer:
    """Analyzes real estate properties for investment potential."""
    
    def __init__(self, market_data: MarketData) -> None:
        """Initialize the analyzer with market data.
        
        Args:
            market_data: Current market statistics and trends
        """
        self.market_data = market_data
    
    def calculate_price_per_sqft(
        self, 
        price: float, 
        square_feet: Optional[int]
    ) -> Optional[float]:
        """Calculate price per square foot for a property.
        
        Args:
            price: Listed price of the property
            square_feet: Total square footage, if available
            
        Returns:
            Price per square foot, or None if square footage unavailable
        """
        if not square_feet or square_feet <= 0:
            logger.warning("Invalid square footage: %s", square_feet)
            return None
            
        return round(price / square_feet, 2)
```

## Questions?

Don't hesitate to ask questions! You can:
- Open an issue with the `question` label
- Reach out via email
- Start a discussion in the repository

Thank you for contributing! 🙏