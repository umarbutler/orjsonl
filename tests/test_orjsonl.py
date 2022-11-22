"""Test the loading, saving, streaming and appending functionality of the orjsonl Python library."""

import orjsonl
from xopen import xopen
import os

data = [
    {'hello': 'world'},
    [1.1, 2.2, 3.3],
    42,
    True,
    None
]

jsonl = '{"hello":"world"}\n'\
        '[1.1,2.2,3.3]\n'\
        '42\n'\
        'true\n'\
        'null\n'\



def test_save() -> None:
    """Test the saving functionality of the orjsonl Python library."""

    orjsonl.save('test_orjsonl.jsonl', data=data)
    with open('test_orjsonl.jsonl', 'r', encoding='utf-8') as file:
        assert file.read() == jsonl

    orjsonl.save('test_orjsonl.jsonl.gz', data=data)
    with xopen('test_orjsonl.jsonl.gz', 'r', encoding='utf-8') as file:
        assert file.read() == jsonl


def test_stream() -> None:
    """Test the streaming functionality of the orjsonl Python library."""

    assert list(orjsonl.stream('test_orjsonl.jsonl')) == data

    assert list(orjsonl.stream('test_orjsonl.jsonl.gz')) == data


def test_load() -> None:
    """Test the loading functionality of the orjsonl Python library."""

    assert orjsonl.load('test_orjsonl.jsonl') == data

    assert orjsonl.load('test_orjsonl.jsonl.gz') == data


def test_append() -> None:
    """Test the appending functionality of the orjsonl Python library."""

    orjsonl.append('test_orjsonl.jsonl', data=[('a', 'b', 'c')])
    with open('test_orjsonl.jsonl', 'r', encoding='utf-8') as file:
        assert file.read() == jsonl + '["a","b","c"]\n'

    with open('test_orjsonl.jsonl', 'a', encoding='utf-8') as file:
        file.write('test')
    orjsonl.append('test_orjsonl.jsonl', data=[{'lorem': 'ipsum'}], newline=False)
    with open('test_orjsonl.jsonl', 'r', encoding='utf-8') as file:
        assert file.read() == jsonl + '["a","b","c"]\ntest\n{"lorem":"ipsum"}\n'

    orjsonl.append('test_orjsonl.jsonl.gz', data=[('a', 'b', 'c')])
    with xopen('test_orjsonl.jsonl.gz', 'r', encoding='utf-8') as file:
        assert file.read() == jsonl + '["a","b","c"]\n'

    with xopen('test_orjsonl.jsonl.gz', 'a', encoding='utf-8') as file:
        file.write('test')
    orjsonl.append('test_orjsonl.jsonl.gz', data=[{'lorem': 'ipsum'}], newline=False)
    with xopen('test_orjsonl.jsonl.gz', 'r', encoding='utf-8') as file:
        assert file.read() == jsonl + '["a","b","c"]\ntest\n{"lorem":"ipsum"}\n'

    os.remove('test_orjsonl.jsonl')
    os.remove('test_orjsonl.jsonl.gz')
