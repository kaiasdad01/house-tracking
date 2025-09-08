"""Example unit tests to validate the testing setup."""

import pytest


class TestExample:
    """Example test class to verify testing framework setup."""
    
    def test_basic_assertion(self):
        """Test basic assertion to verify pytest is working."""
        assert 1 + 1 == 2
    
    def test_with_fixture(self, sample_property_data):
        """Test using a fixture."""
        assert sample_property_data["bedrooms"] == 3
        assert sample_property_data["bathrooms"] == 2
        assert "Lafayette" in sample_property_data["address"]
    
    @pytest.mark.parametrize("price,expected_range", [
        (750000, "high"),
        (500000, "medium"),
        (300000, "low"),
    ])
    def test_parametrized_price_categorization(self, price, expected_range):
        """Test price categorization with parameters."""
        if price > 700000:
            category = "high"
        elif price > 400000:
            category = "medium"
        else:
            category = "low"
        
        assert category == expected_range


def test_sample_calculations():
    """Test some basic calculations that might be used in the app."""
    # Price per square foot calculation
    price = 750000
    sqft = 2100
    price_per_sqft = round(price / sqft, 2)
    
    assert price_per_sqft == 357.14
    
    # Days on market categorization
    days_on_market = 15
    if days_on_market < 7:
        market_speed = "fast"
    elif days_on_market < 30:
        market_speed = "normal"
    else:
        market_speed = "slow"
    
    assert market_speed == "normal"