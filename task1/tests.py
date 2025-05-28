import pytest
from solution import strict


def test_correct_types():
    @strict
    def add(a: int, b: int) -> int:
        return a + b

    assert add(1, 2) == 3


def test_incorrect_types():
    @strict
    def add(a: int, b: int) -> int:
        return a + b

    with pytest.raises(TypeError, match="b must be int, got float"):
        add(1, 2.4)

    with pytest.raises(TypeError, match="a must be int, got str"):
        add("1", 2)


def test_keyword_arguments():
    @strict
    def greet(name: str, age: int) -> str:
        return f"{name} is {age} years old"

    assert greet(name="Alice", age=25) == "Alice is 25 years old"

    with pytest.raises(TypeError, match="age must be int, got str"):
        greet(name="Bob", age="25")


def test_bool_type():
    @strict
    def invert(flag: bool) -> bool:
        return not flag

    assert invert(True) is False

    with pytest.raises(TypeError, match="flag must be bool, got int"):
        invert(1)


def test_mixed_arguments():
    @strict
    def mixed(a: int, b: float, c: str) -> str:
        return f"{a} {b} {c}"

    assert mixed(1, 2.0, "3") == "1 2.0 3"
    assert mixed(a=1, b=2.0, c="3") == "1 2.0 3"

    with pytest.raises(TypeError, match="a must be int, got float"):
        mixed(1.0, 2.0, "3")

    with pytest.raises(TypeError, match="b must be float, got int"):
        mixed(1, 2, 3)
