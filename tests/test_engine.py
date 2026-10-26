from src.engine import analyze

def test_positive():
    assert analyze("Excellent quality and fast delivery")["sentiment"] == "positive"

def test_negative():
    assert analyze("Broken product and terrible service")["sentiment"] == "negative"

def test_neutral():
    assert analyze("Package arrived this afternoon")["sentiment"] == "neutral"

def test_empty():
    import pytest
    with pytest.raises(ValueError):
        analyze("  ")

def test_schema():
    result = analyze("Refund has not arrived after weeks")
    assert set(result) == {"review","sentiment","confidence","urgent","signals","needs_review"}
    assert 0 <= result["confidence"] <= 1

def test_urgent():
    result = analyze("Broken product and terrible service")
    assert result["urgent"] is True
