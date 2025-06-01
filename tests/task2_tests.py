import pytest
from unittest.mock import patch
from task2.solution import get_animals_count


def test_get_animals_count():
    mock_html = """
    <div class="mw-category-columns">
        <h3>A</h3>
        <div><a href="/ant">Ant</a><a href="/ape">Ape</a></div>
        <h3>B</h3>
        <div><a href="/bear">Bear</a></div>
    </div>
    """
    with patch('requests.get') as mock_get:
        mock_get.return_value.text = mock_html
        result = get_animals_count()
    assert result == {'A': 2, 'B': 1}


def test_single_page_scraping():
    mock_html = """
    <div class="mw-category">
        <h3>Z</h3>
        <div><a href="/zebra">Zebra</a></div>
    </div>
    """
    with patch('requests.get') as mock_get:
        mock_get.return_value.text = mock_html
        result = get_animals_count()
    assert result == {'Z': 1}
