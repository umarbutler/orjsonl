# orjsonl

<a href="https://pypi.org/project/orjsonl/" alt="PyPI Version"><img src="https://img.shields.io/pypi/v/orjsonl"></a> <a href="https://github.com/umarbutler/orjsonl/actions/workflows/ci.yml" alt="Build Status"><img src="https://img.shields.io/github/workflow/status/umarbutler/orjsonl/ci"></a> <a href="https://app.codecov.io/gh/umarbutler/orjsonl" alt="Code Coverage"><img src="https://img.shields.io/codecov/c/github/umarbutler/orjsonl"></a> <a href="https://pypistats.org/packages/orjsonl" alt="Downloads"><img src="https://img.shields.io/pypi/dm/orjsonl"></a>

orjsonl is a simple, fast and lightweight Python library for loading, saving, streaming and appending [jsonl](https://jsonlines.org/) (also known as JSON Lines) files. It is powered by [orjson](https://github.com/ijl/orjson), the quickest and most correct json serializer currently available for Python.

## Installation

orjsonl may be installed with `pip`:

```bash
pip install orjsonl
```

## Usage

This code snippet demonstrates how jsonl files can be loaded, saved, appended and streamed with the [`load()`](#load), [`save()`](#save), [`append()`](#append) and [`stream()`](#stream) functions, respectively:

```python
>>> import orjsonl
>>> data = [
    {'hello' : 'world'},
    [1.1, 2.2, 3.3],
    42,
    True,
    None
]
>>> orjsonl.save(path='test.jsonl', data=data)
>>> orjsonl.load(path='test.jsonl')
[{'hello': 'world'}, [1.1, 2.2, 3.3], 42, True, None]
>>> orjsonl.append(path='test.jsonl', data=[('a', 'b', 'c')])
>>> [object_ for object_ in orjsonl.stream(path='test.jsonl')]
[{'hello': 'world'}, [1.1, 2.2, 3.3], 42, True, None, ['a', 'b', 'c']]
```

### Load

```python
def load(
    path: str | bytes | int | os.PathLike
) -> list[dict | list | int | float | str | bool | None]: ...
```

[`load()`](#load) deserializes a UTF-8-encoded jsonl file to a list of Python objects.

The only argument taken by this function is `path`, a path-like object giving the pathname (absolute or relative to the current working directory), or an integer file descriptor, of the jsonl file to be deserialized.

This function returns a `list` object comprised of deserialized `dict`, `list`, `int`, `float`, `str`, `bool` or `None` objects.

### Stream

```python
def stream(
    path: str | bytes | int | os.PathLike
) -> map: ...
```

[`stream()`](#stream) creates a `map` object that deserializes a UTF-8-encoded jsonl file to Python objects.

The only argument taken by this function is `path`, a path-like object giving the pathname (absolute or relative to the current working directory), or an integer file descriptor, of the jsonl file to be deserialized by the `map` object.

This function returns a `map` object that deserializes the jsonl file to `dict`, `list`, `int`, `float`, `str`, `bool` or `None` objects.

### Save

```python
def save(
    path: str | bytes | int | os.PathLike,
    data: Iterable
) -> None: ...
```

[`save()`](#save) serializes an iterable of Python objects to a UTF-8-encoded jsonl file.

The first argument taken by this function is `path`, a path-like object giving the pathname (absolute or relative to the current working directory), or an integer file descriptor, of the jsonl file to be saved.

The second argument taken by this function is `data`, an iterable of Python objects to be serialized to the jsonl file.

### Append

```python
def append(
    path: str | bytes | int | os.PathLike,
    data: Iterable,
    newline: bool = True
) -> None: ...
```

[`append()`](#append) serializes and appends an iterable of Python objects to a UTF-8-encoded jsonl file.

The first argument taken by this function is `path`, a path-like object giving the pathname (absolute or relative to the current working directory), or an integer file descriptor, of the jsonl file to be appended.

The second argument taken by this function is `data`, an iterable of Python objects to be serialized and appended to the jsonl file.

The third argument taken by this function is `newline`, an optional Boolean flag that, if set to `False`, indicates that the jsonl file does not end with a newline and should, therefore, have one added before data is appended.

## License

This library is licensed under the [MIT License](https://github.com/umarbutler/orjsonl/blob/main/LICENSE).
