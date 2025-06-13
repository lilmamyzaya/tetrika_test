def strict(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        arg_names = func.__code__.co_varnames[:func.__code__.co_argcount]

        for name, value in zip(arg_names, args):
            if name in annotations and not isinstance(value, annotations[name]):
                raise TypeError(
                    f"Argument '{name}' must be of type {annotations[name]}, not {type(value)}"
                )

        for name, value in kwargs.items():
            if name in annotations and not isinstance(value, annotations[name]):
                raise TypeError(
                    f"Argument '{name}' must be of type {annotations[name]}, not {type(value)}"
                )

        return func(*args, **kwargs)

    return wrapper


if __name__ == "__main__":
    @strict
    def sum_two(a: int, b: int) -> int:
        return a + b

    assert sum_two(1, 2) == 3

    try:
        sum_two(1, 2.4)
        assert False, "Expected TypeError"
    except TypeError:
        pass

    try:
        sum_two("1", "2")
        assert False, "Expected TypeError"
    except TypeError:
        pass

    print("All tests passed!")