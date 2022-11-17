"""Test the loading, saving, streaming and appending functionality of the orjsonl Python library."""

import orjsonl
import os

data = [
    {"hello": "world"},
    [1.1, 2.2, 3.3],
    42,
    True,
    None
]

jsonl = '{"hello":"world"}\n'\
        "[1.1,2.2,3.3]\n"\
        "42\n"\
        "true\n"\
        "null\n"\

open('test_orjsonl.jsonl', 'w', encoding='utf-8').write(jsonl)


def test_stream() -> None:
    """Test the streaming functionality of the orjsonl Python library."""

    assert list(orjsonl.stream('test_orjsonl.jsonl')) == data


def test_load() -> None:
    """Test the loading functionality of the orjsonl Python library."""

    assert orjsonl.load('test_orjsonl.jsonl') == data


def test_save() -> None:
    """Test the saving functionality of the orjsonl Python library."""

    orjsonl.save(path='test_orjsonl.jsonl', data=data)
    assert open('test_orjsonl.jsonl', 'r', encoding='utf-8').read() == jsonl


def test_append() -> None:
    """Test the appending functionality of the orjsonl Python library."""

    orjsonl.append(path='test_orjsonl.jsonl', data=[("a", "b", "c")])
    assert open('test_orjsonl.jsonl', 'r', encoding='utf-8').read() == jsonl + '["a","b","c"]\n'

    open('test_orjsonl.jsonl', 'a', encoding='utf-8').write('test')
    orjsonl.append(path='test_orjsonl.jsonl', data=[{"lorem": "ipsum"}], newline=False)
    assert open('test_orjsonl.jsonl', 'r', encoding='utf-8').read() == jsonl + '["a","b","c"]\ntest\n{"lorem":"ipsum"}\n'

    os.remove('test_orjsonl.jsonl')
