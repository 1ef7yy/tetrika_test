import pytest
import csv
import solution

def test_get_animals_count():
    counts = solution.get_animals_count()
    assert isinstance(counts, dict)
    assert all(key in counts for key in 'АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')

    assert any(value > 0 for value in counts.values())

def test_write_to_csv(tmp_path):
    counts = {'А': 10, 'Б': 20}
    solution.write_to_csv(counts)
    csv_file = tmp_path / 'beasts.csv'
    assert csv_file.exists()

    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    assert rows == [['А', '10'], ['Б', '20']]

def test_write_to_csv_with_empty_counts(tmp_path):
    counts = {}
    solution.write_to_csv(counts)
    csv_file = tmp_path / 'beasts.csv'
    assert csv_file.exists()

    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    assert rows == []
