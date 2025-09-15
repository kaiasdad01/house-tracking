# Real Estate Tracker 

A comprehensive home buying analysis tool designed for first-time buyers who want to stay on top of their search with automated analysis and insights.

##  Problem Statement

As first-time home buyers with busy schedules, it's challenging to keep up with listings, price changes, and market analysis. This tool automates the tedious parts of home searching while providing data-driven insights to help make informed decisions.

##  Features

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

## Architecture

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


## Data Sources
- **Realtor.com API**: Additional listings and property details  

## Tech Stack

- **Backend**: FastAPI, SQLAlchemy, Pydantic
- **Frontend**: Streamlit, Plotly
- **Data Pipeline**: Prefect, dbt
- **Storage**: Google BigQuery, PostgreSQL
- **Caching**: Redis
- **Testing**: pytest, factory-boy
- **Code Quality**: black, isort, flake8, mypy, pre-commit
