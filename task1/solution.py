def strict(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        # позиционные аргументы
        for name, value in zip(func.__code__.co_varnames, args):
            if name in annotations:
                expected = annotations[name]
                if not isinstance(value, expected):
                    raise TypeError(
                        f"{name} must be {expected.__name__}, got {type(value).__name__}"
                    )

        # именнованные
        for name, value in kwargs.items():
            if name in annotations:
                expected = annotations[name]
                if not isinstance(value, expected):
                    raise TypeError(
                        f"{name} must be {expected.__name__}, got {type(value).__name__}"
                    )

        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    print(sum_two(1, 2))  # >>> 3
    print(sum_two(1, 2.4))  # >>> TypeError
