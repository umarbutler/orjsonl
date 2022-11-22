# orjsonl

<a href="https://pypi.org/project/orjsonl/" alt="PyPI Version"><img src="https://img.shields.io/pypi/v/orjsonl"></a> <a href="https://github.com/umarbutler/orjsonl/actions/workflows/ci.yml" alt="Build Status"><img src="https://img.shields.io/github/workflow/status/umarbutler/orjsonl/ci"></a> <a href="https://app.codecov.io/gh/umarbutler/orjsonl" alt="Code Coverage"><img src="https://img.shields.io/codecov/c/github/umarbutler/orjsonl"></a> <a href="https://pypistats.org/packages/orjsonl" alt="Downloads"><img src="https://img.shields.io/pypi/dm/orjsonl"></a>

`orjsonl` is a simple, fast and lightweight Python library for loading, saving, streaming and appending both compressed and uncompressed [jsonl](https://jsonlines.org/) (also known as ‘json lines’, ‘newline-delimited json’ and ‘ndjson’) files. It is powered by [`orjson`](https://github.com/ijl/orjson), the quickest and most correct json serializer currently available for Python.

## Installation

`orjsonl` may be installed with `pip`:

```bash
pip install orjsonl
```

To read or write Zstandard files, you must also install either [`zstd`](https://github.com/facebook/zstd) or the [`zstandard`](https://pypi.org/project/zstandard/) Python package.

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
>>> orjsonl.save('test.jsonl', data)
>>> orjsonl.load('test.jsonl')
[{'hello': 'world'}, [1.1, 2.2, 3.3], 42, True, None]
>>> orjsonl.append('test.jsonl', [('a', 'b', 'c')])
>>> [object_ for object_ in orjsonl.stream('test.jsonl')]
[{'hello': 'world'}, [1.1, 2.2, 3.3], 42, True, None, ['a', 'b', 'c']]
```

The exact same functions can also be used to process jsonl files compressed with gzip, bzip2, xz and Zstandard:

```python
>>> import orjsonl
>>> data = [
    {'hello' : 'world'},
    [1.1, 2.2, 3.3],
    42,
    True,
    None
]
>>> orjsonl.save('test.jsonl.gz', data)
>>> orjsonl.load('test.jsonl.gz')
[{'hello': 'world'}, [1.1, 2.2, 3.3], 42, True, None]
>>> orjsonl.append('test.jsonl.gz', [('a', 'b', 'c')])
>>> [object_ for object_ in orjsonl.stream('test.jsonl.gz')]
[{'hello': 'world'}, [1.1, 2.2, 3.3], 42, True, None, ['a', 'b', 'c']]
```

### Load

```python
def load(
    path: str | bytes | int | os.PathLike,
    decompression_threads: Optional[int] = None,
    compression_format: Optional[str] = None
) -> list[dict | list | int | float | str | bool | None]: ...
```

`load()` deserializes a compressed or uncompressed UTF-8-encoded jsonl file to a list of Python objects.

`path` is a path-like object giving the pathname (absolute or relative to the current working directory) of the compressed or uncompressed UTF-8-encoded jsonl file to be deserialized.

`decompression_threads` is an optional integer passed to [`xopen.xopen()`](https://github.com/pycompression/xopen/#xopen) as the [`threads`](https://github.com/pycompression/xopen/#xopen) argument that specifies the number of threads that should be used for decompression.

`compression_format` is an optional string passed to [`xopen.xopen()`](https://github.com/pycompression/xopen/#xopen) as the [`format`](https://github.com/pycompression/xopen/#v130-2022-01-10) argument that overrides the autodetection of the file’s compression format based on its extension or content. Possible values are ‘gz’, ‘xz’, ‘bz2’ and ‘zst’.

This function returns a `list` object comprised of deserialized `dict`, `list`, `int`, `float`, `str`, `bool` or `None` objects.

### Stream

```python
def stream(
    path: str | bytes | int | os.PathLike,
    decompression_threads: Optional[int] = None,
    compression_format: Optional[str] = None
) -> Generator[dict | list | int | float | str | bool | None, None, None]: ...
```

`stream()` creates a `generator` that deserializes a compressed or uncompressed UTF-8-encoded jsonl file to Python objects.

`path` is a path-like object giving the pathname (absolute or relative to the current working directory) of the compressed or uncompressed UTF-8-encoded jsonl file to be deserialized by the `generator`.

`decompression_threads` is an optional integer passed to [`xopen.xopen()`](https://github.com/pycompression/xopen/#xopen) as the [`threads`](https://github.com/pycompression/xopen/#xopen) argument that specifies the number of threads that should be used for decompression.

`compression_format` is an optional string passed to [`xopen.xopen()`](https://github.com/pycompression/xopen/#xopen) as the [`format`](https://github.com/pycompression/xopen/#v130-2022-01-10) argument that overrides the autodetection of the file’s compression format based on its extension or content. Possible values are ‘gz’, ‘xz’, ‘bz2’ and ‘zst’.

This function returns a `generator` that deserializes the file to `dict`, `list`, `int`, `float`, `str`, `bool` or `None` objects.

### Save

```python
def save(
    path: str | bytes | int | os.PathLike,
    data: Iterable,
    default: Optional[Callable] = None,
    option: int = 0,
    compression_level: Optional[int] = None,
    compression_threads: Optional[int] = None,
    compression_format: Optional[str] = None
) -> None: ...
```

`save()` serializes an iterable of Python objects to a compressed or uncompressed UTF-8-encoded jsonl file.

`path` is a path-like object giving the pathname (absolute or relative to the current working directory) of the compressed or uncompressed UTF-8-encoded jsonl file to be saved.

`data` is an iterable of Python objects to be serialized to the file.

`default` is an optional callable passed to [`orjson.dumps()`](https://github.com/ijl/orjson#serialize) as the [`default`](https://github.com/ijl/orjson#default) argument that serializes subclasses or arbitrary types to a supported type.

`option` is an optional integer passed to [`orjson.dumps()`](https://github.com/ijl/orjson#serialize) as the [`option`](https://github.com/ijl/orjson#option) argument that modifies how data is serialized.

`compression_level` is an optional integer passed to [`xopen.xopen()`](https://github.com/pycompression/xopen/#xopen) as the `compresslevel` argument that determines the compression level for writing to gzip, xz and zstandard files.

`decompression_threads` is an optional integer passed to [`xopen.xopen()`](https://github.com/pycompression/xopen/#xopen) as the [`threads`](https://github.com/pycompression/xopen/#xopen) argument that specifies the number of threads that should be used for compression.

`compression_format` is an optional string passed to [`xopen.xopen()`](https://github.com/pycompression/xopen/#xopen) as the [`format`](https://github.com/pycompression/xopen/#v130-2022-01-10) argument that overrides the autodetection of the file’s compression format based on its extension. Possible values are ‘gz’, ‘xz’, ‘bz2’ and ‘zst’.

### Append

```python
def append(
    path: str | bytes | int | os.PathLike,
    data: Iterable,
    newline: bool = True,
    default: Optional[Callable] = None,
    option: int = 0,
    compression_level: Optional[int] = None,
    compression_threads: Optional[int] = None,
    compression_format: Optional[str] = None
) -> None: ...
```

`append()` serializes and appends an iterable of Python objects to a UTF-8-encoded jsonl file.

`path` is a path-like object giving the pathname (absolute or relative to the current working directory) of the compressed or uncompressed UTF-8-encoded jsonl file to be appended.

`data` is an iterable of Python objects to be serialized and appended to the file.

`newline` is an optional Boolean flag that, if set to `False`, indicates that the file does not end with a newline and should, therefore, have one added before data is appended.

`default` is an optional callable passed to [`orjson.dumps()`](https://github.com/ijl/orjson#serialize) as the [`default`](https://github.com/ijl/orjson#default) argument that serializes subclasses or arbitrary types to a supported type.

`option` is an optional integer passed to [`orjson.dumps()`](https://github.com/ijl/orjson#serialize) as the [`option`](https://github.com/ijl/orjson#option) argument that modifies how data is serialized.

`compression_level` is an optional integer passed to [`xopen.xopen()`](https://github.com/pycompression/xopen/#xopen) as the `compresslevel` argument that determines the compression level for writing to gzip, xz and zstandard files.

`decompression_threads` is an optional integer passed to [`xopen.xopen()`](https://github.com/pycompression/xopen/#xopen) as the [`threads`](https://github.com/pycompression/xopen/#xopen) argument that specifies the number of threads that should be used for compression.

`compression_format` is an optional string passed to [`xopen.xopen()`](https://github.com/pycompression/xopen/#xopen) as the [`format`](https://github.com/pycompression/xopen/#v130-2022-01-10) argument that overrides the autodetection of the file’s compression format based on its extension or content. Possible values are ‘gz’, ‘xz’, ‘bz2’ and ‘zst’.

## License

This library is licensed under the [MIT License](https://github.com/umarbutler/orjsonl/blob/main/LICENSE).
