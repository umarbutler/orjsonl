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

`load()` deserializes a UTF-8-encoded jsonl file to a list of Python objects.

`path` is a path-like object giving the pathname (absolute or relative to the current working directory), or an integer file descriptor, of the jsonl file to be deserialized.

This function returns a `list` object comprised of deserialized `dict`, `list`, `int`, `float`, `str`, `bool` or `None` objects.

### Stream

```python
def stream(
    path: str | bytes | int | os.PathLike
) -> map: ...
```

`stream()` creates a `map` object that deserializes a UTF-8-encoded jsonl file to Python objects.

`path` is a path-like object giving the pathname (absolute or relative to the current working directory), or an integer file descriptor, of the jsonl file to be deserialized by the `map` object.

This function returns a `map` object that deserializes the jsonl file to `dict`, `list`, `int`, `float`, `str`, `bool` or `None` objects.

### Save

```python
def save(
    path: str | bytes | int | os.PathLike,
    data: Iterable,
    default: Callable = None,
    option: int = 0
) -> None: ...
```

`save()` serializes an iterable of Python objects to a UTF-8-encoded jsonl file.

`path` is a path-like object giving the pathname (absolute or relative to the current working directory), or an integer file descriptor, of the jsonl file to be saved.

`data` is an iterable of Python objects to be serialized to the jsonl file.

`default` is an optional callable passed to [`orjson.dumps()`](https://github.com/ijl/orjson#serialize) as the [`default`](https://github.com/ijl/orjson#default) argument that serializes a subclass or arbitrary types to a supported type.

`option` is an optional integer passed to [`orjson.dumps()`](https://github.com/ijl/orjson#serialize) as the [`option`](https://github.com/ijl/orjson#option) argument that modifies how data is serialized.

### Append

```python
def append(
    path: str | bytes | int | os.PathLike,
    data: Iterable,
    newline: bool = True,
    default: Callable = None,
    option: int = 0
) -> None: ...
```

`append()` serializes and appends an iterable of Python objects to a UTF-8-encoded jsonl file.

`path` is a path-like object giving the pathname (absolute or relative to the current working directory), or an integer file descriptor, of the jsonl file to be appended.

`data` is an iterable of Python objects to be serialized and appended to the jsonl file.

`newline` is an optional Boolean flag that, if set to `False`, indicates that the jsonl file does not end with a newline and should, therefore, have one added before data is appended.

`default` is an optional callable passed to [`orjson.dumps()`](https://github.com/ijl/orjson#serialize) as the [`default`](https://github.com/ijl/orjson#default) argument that serializes a subclass or arbitrary types to a supported type.

`option` is an optional integer passed to [`orjson.dumps()`](https://github.com/ijl/orjson#serialize) as the [`option`](https://github.com/ijl/orjson#option) argument that modifies how data is serialized.

## License

This library is licensed under the [MIT License](https://github.com/umarbutler/orjsonl/blob/main/LICENSE).
