# Real Estate Tracker 🏠

A comprehensive home buying analysis tool designed for first-time buyers who want to stay on top of their search with automated analysis and insights.

## 🎯 Problem Statement

As first-time home buyers with busy schedules, it's challenging to keep up with listings, price changes, and market analysis. This tool automates the tedious parts of home searching while providing data-driven insights to help make informed decisions.

## ✨ Features

### MVP (Current)
- **User Onboarding**: Set preferences for beds, baths, square footage, and locations
- **Automated Listing Collection**: Scan multiple data sources 3x daily for new listings
- **Change Tracking**: Monitor price changes, status updates, and market events
- **Smart Analysis**: Calculate price per square foot, days on market, and trend indicators  
- **Interactive Dashboard**: View all matching properties with key metrics and filters
- **Personal Notes**: Track thoughts and observations for each property

### Planned Features
- Real-time notifications for new listings and price changes
- Market trend analysis and predictions
- Commute time analysis to important locations
- School district and neighborhood insights
- Investment potential scoring

## 🏗️ Architecture

```
├── src/real_estate_tracker/
│   ├── api/                 # FastAPI endpoints
│   ├── data/               # Data ingestion and processing
│   ├── models/             # Pydantic models and database schemas
│   ├── services/           # Business logic and external API integrations
│   └── ui/                 # Streamlit user interface
├── tests/
│   ├── unit/               # Unit tests
│   └── integration/        # Integration tests
├── dbt/                    # Data transformation models
├── config/                 # Configuration files
└── docs/                   # Documentation
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Google Cloud Platform account (for BigQuery)
- API keys for real estate data sources

### Development Setup

1. **Clone and setup environment:**
   ```bash
   git clone <your-repo-url>
   cd real-estate-tracker
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

2. **Install dependencies:**
   ```bash
   make install-dev
   # or manually:
   pip install -r requirements-dev.txt
   ```

3. **Configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and configuration
   ```

4. **Set up pre-commit hooks:**
   ```bash
   pre-commit install
   ```

### Running the Application

1. **Start the API server:**
   ```bash
   make run-api
   # Access at http://localhost:8000
   ```

2. **Start the UI (in another terminal):**
   ```bash
   make run-ui
   # Access at http://localhost:8501
   ```

3. **Run data collection:**
   ```bash
   make run-scraper
   ```

## 🧪 Testing

```bash
# Run all tests
make test

# Run with coverage
make test-cov

# Run specific test types
make test-unit
make test-integration
```

## 🔧 Development

### Code Quality
```bash
# Format code
make format

# Run linting
make lint

# Type checking
make type-check

# Run all pre-commit hooks
make pre-commit
```

### Database Operations
```bash
# Run migrations
make db-migrate

# Create new migration
make db-revision MESSAGE="your migration message"
```

### dbt Operations
```bash
# Install dbt dependencies
make dbt-deps

# Run data transformations
make dbt-run

# Test data quality
make dbt-test
```

## 📊 Data Sources

- **Zillow API**: Primary listing data and market insights
- **Realtor.com API**: Additional listings and property details  
- **Redfin API**: Market trends and pricing data

## 🛠️ Tech Stack

- **Backend**: FastAPI, SQLAlchemy, Pydantic
- **Frontend**: Streamlit, Plotly
- **Data Pipeline**: Prefect, dbt
- **Storage**: Google BigQuery, PostgreSQL
- **Caching**: Redis
- **Testing**: pytest, factory-boy
- **Code Quality**: black, isort, flake8, mypy, pre-commit

## 📝 API Documentation

When running the API server, visit:
- **Interactive docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linting (`make test lint`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guide
- Write tests for new features
- Update documentation as needed
- Use conventional commit messages
- Ensure all CI checks pass

## 📋 User Personas

### Jillian - The Analytical First-Time Buyer
- **Profile**: Busy professional, highly analytical, looking for sound investment decisions
- **Location**: Lafayette, CO
- **Criteria**: 3+ beds, 2+ baths, $600k-$1M
- **Needs**: Automated searching and analysis without deep manual research

### Kaia - The Real Estate Investor
- **Profile**: Experienced in real estate investing, looking for new opportunities
- **Needs**: Market trend analysis, ROI calculations, portfolio optimization

## 🗺️ Roadmap

### Phase 1: Foundation (Weeks 1-2) ✅
- [x] Project setup and configuration
- [x] Basic data pipeline architecture
- [x] Development environment setup

### Phase 2: Data Collection (Weeks 2-3)
- [ ] API integrations for listing data
- [ ] Automated data collection pipeline
- [ ] Change detection and tracking

### Phase 3: MVP UI (Weeks 3-4)
- [ ] User onboarding flow
- [ ] Listings dashboard
- [ ] Basic filtering and search

### Phase 4: Analysis & Features (Weeks 4-5)
- [ ] Market analysis calculations
- [ ] Notification system
- [ ] Advanced filtering and insights

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

For questions or issues:
- Create an issue in this repository
- Email: your.email@example.com
- LinkedIn: [Your LinkedIn Profile]

---

**Built with ❤️ by Matthew Dwyer**