from typing import (
    Union,
    Generator,
    List,
    Optional,
    Callable
)
import os
from xopen import xopen
import orjson
from collections.abc import Iterable


def stream(
    path: Union[str, bytes, os.PathLike],
    decompression_threads: Optional[int] = None,
    compression_format: Optional[str] = None
) -> Generator[Union[dict, list, int, float, str, bool, None], None, None]:
    """Create a generator that deserializes a compressed or uncompressed UTF-8-encoded jsonl file to Python objects.

    Args:
        path (str | bytes | os.PathLike): A path-like object giving the pathname (absolute or relative to the current working directory) of the compressed or uncompressed UTF-8-encoded jsonl file to be deserialized by the generator.
        decompression_threads (int, optional): An optional integer passed to xopen.xopen() as the 'threads' argument that specifies the number of threads that should be used for decompression. Defaults to None.
        compression_format (str, optional): An optional string passed to xopen.xopen() as the 'format' argument that overrides the autodetection of the file's compression format based on its extension or content. Possible values are 'gz', 'xz', 'bz2' and 'zst'. Defaults to None.

    Returns:
        Generator[dict | list | int | float | str | bool | None, None, None]: A generator that deserializes the file to Python objects."""

    with xopen(path, 'rb', threads=decompression_threads, format=compression_format) as file:
        for json in file:
            yield orjson.loads(json)


def load(
    path: Union[str, bytes, os.PathLike],
    decompression_threads: Optional[int] = None,
    compression_format: Optional[str] = None
) -> List[Union[dict, list, int, float, str, bool, None]]:
    """Deserialize a compressed or uncompressed UTF-8-encoded jsonl file to a list of Python objects.

    Args:
        path (str | bytes | os.PathLike): A path-like object giving the pathname (absolute or relative to the current working directory) of the compressed or uncompressed UTF-8-encoded jsonl file to be deserialized.
        decompression_threads (int, optional): An optional integer passed to xopen.xopen() as the 'threads' argument that specifies the number of threads that should be used for decompression. Defaults to None.
        compression_format (str, optional): An optional string passed to xopen.xopen() as the 'format' argument that overrides the autodetection of the file's compression format based on its extension or content. Possible values are 'gz', 'xz', 'bz2' and 'zst'. Defaults to None.

    Returns:
        list[dict | list | int | float | str | bool | None]: A list of deserialized objects."""

    with xopen(path, 'rb', threads=decompression_threads, format=compression_format) as file:
        return [orjson.loads(json) for json in file]


def save(
    path: Union[str, bytes, os.PathLike],
    data: Iterable,
    default: Optional[Callable] = None,
    option: int = 0,
    compression_level: Optional[int] = None,
    compression_threads: Optional[int] = None,
    compression_format: Optional[str] = None
) -> None:
    """Serialize an iterable of Python objects to a compressed or uncompressed UTF-8-encoded jsonl file.

    Args:
        path (str | bytes | os.PathLike): A path-like object giving the pathname (absolute or relative to the current working directory) of the compressed or uncompressed UTF-8-encoded jsonl file to be saved.
        data (Iterable): An iterable of Python objects to be serialized to the file.
        default (Callable, optional): An optional callable passed to orjson.dumps() as the 'default' argument that serializes subclasses or arbitrary types to a supported type. Defaults to None.
        option (int, optional): An optional integer passed to orjson.dumps() as the 'option' argument that modifies how data is serialized. Defaults to 0.
        compression_level (int, optional): An optional integer passed to xopen.xopen() as the 'compresslevel' argument that determines the compression level for writing to gzip, xz and zstandard files. Defaults to None.
        compression_threads (int, optional): An optional integer passed to xopen.xopen() as the 'threads' argument that specifies the number of threads that should be used for compression. Defaults to None.
        compression_format (str, optional): An optional string passed to xopen.xopen() as the 'format' argument that overrides the autodetection of the file's compression format based on its extension. Possible values are 'gz', 'xz', 'bz2' and 'zst'. Defaults to None."""

    with xopen(path, 'wb', compresslevel=compression_level, threads=compression_threads, format=compression_format) as writer:
        for item in data:
            writer.write(orjson.dumps(item, default=default, option=option))
            writer.write(b'\n')


def append(
    path: Union[str, bytes, os.PathLike],
    data: Iterable,
    newline: Optional[bool] = True,
    default: Optional[Callable] = None,
    option: int = 0,
    compression_level: Optional[int] = None,
    compression_threads: Optional[int] = None,
    compression_format: Optional[str] = None
) -> None:
    """Serialize and append an iterable of Python objects to a compressed or uncompressed UTF-8-encoded jsonl file.

    Args:
        path (str | bytes | os.PathLike): A path-like object giving the pathname (absolute or relative to the current working directory) of the compressed or uncompressed UTF-8-encoded jsonl file to be appended.
        data (Iterable): An iterable of Python objects to be serialized and appended to the file.
        newline (bool, optional): An optional Boolean flag that, if set to False, indicates that the file does not end with a newline and should, therefore, have one added before data is appended. Defaults to True.
        default (Callable, optional): An optional callable passed to orjson.dumps() as the 'default' argument that serializes subclasses or arbitrary types to a supported type. Defaults to None.
        option (int, optional): An optional integer passed to orjson.dumps() as the 'option' argument that modifies how data is serialized. Defaults to 0.
        compression_level (int, optional): An optional integer passed to xopen.xopen() as the 'compresslevel' argument that determines the compression level for writing to gzip, xz and zstandard files. Defaults to None.
        compression_threads (int, optional): An optional integer passed to xopen.xopen() as the 'threads' argument that specifies the number of threads that should be used for compression. Defaults to None.
        compression_format (str, optional): An optional string passed to xopen.xopen() as the 'format' argument that overrides the autodetection of the file's compression format based on its extension or content. Possible values are 'gz', 'xz', 'bz2' and 'zst'. Defaults to None."""

    with xopen(path, 'ab', compresslevel=compression_level, threads=compression_threads, format=compression_format) as writer:
        if not newline:
            writer.write(b'\n')

        for item in data:
            writer.write(orjson.dumps(item, default=default, option=option))
            writer.write(b'\n')
