"""A simple, fast and lightweight Python library for loading, saving, streaming and appending jsonl (also known as JSON Lines) files."""

from typing import Union, List
import os
from collections.abc import Iterable
import orjson


def stream(path: Union[str, bytes, int, os.PathLike]) -> map:
    """Create a map object that deserializes a UTF-8-encoded jsonl file to Python objects.

    Args:
        path (str | bytes | int | os.PathLike): A path-like object giving the pathname (absolute or relative to the current working directory), or an integer file descriptor, of the jsonl file to be deserialized by the map object.

    Returns:
        map: A map object that deserializes a jsonl file to Python objects."""

    return map(orjson.loads, open(path, 'rb'))


def load(path: Union[str, bytes, int, os.PathLike]) -> List[Union[dict, list, int, float, str, bool, None]]:
    """Deserialize a UTF-8-encoded jsonl file to a list of Python objects.

    Args:
        path (str | bytes | int | os.PathLike): A path-like object giving the pathname (absolute or relative to the current working directory), or an integer file descriptor, of the jsonl file to be deserialized.

    Returns:
        list[dict | list | int | float | str | bool | None]: A list of deserialized objects."""

    return list(stream(path))


def save(path: Union[str, bytes, int, os.PathLike], data: Iterable) -> None:
    """Serialize an iterable of Python objects to a UTF-8-encoded jsonl file.

    Args:
        path (str | bytes | int | os.PathLike): A path-like object giving the pathname (absolute or relative to the current working directory), or an integer file descriptor, of the jsonl file to be saved.
        data (Iterable): An iterable of Python objects to be serialized to the jsonl file."""

    with open(path, 'wb') as writer:
        for item in data:
            writer.write(orjson.dumps(item))
            writer.write(b'\n')


def append(path: Union[str, bytes, int, os.PathLike], data: Iterable, newline: bool = True) -> None:
    """Serialize and append an iterable of Python objects to a UTF-8-encoded jsonl file.

    Args:
        path (str | bytes | int | os.PathLike): A path-like object giving the pathname (absolute or relative to the current working directory), or an integer file descriptor, of the jsonl file to be appended.
        data (Iterable): An iterable of Python objects to be serialized and appended to the jsonl file.
        newline (bool, optional): An optional Boolean flag that, if set to False, indicates that the jsonl file does not end with a newline and should, therefore, have one added before data is appended. Defaults to True."""

    with open(path, 'ab') as writer:
        if not newline:
            writer.write(b'\n')

        for item in data:
            writer.write(orjson.dumps(item))
            writer.write(b'\n')
