"""Test orjsonl."""

import orjsonl
import helpers
import orjson

DATA = [
    'hello world',
    ['fizz', 'buzz'],
]

JSONL = """\
"hello world"
["fizz","buzz"]
"""


def test_save(tmp_path):
    """Test `orjsonl.save()`."""

    orjsonl.save(tmp_path / 'test_orjsonl.jsonl', data=DATA)
    assert helpers.load(tmp_path / 'test_orjsonl.jsonl') == JSONL.encode('utf-8')


def test_load(tmp_path) -> None:
    """Test `orjsonl.load()`."""
    
    helpers.save(tmp_path / 'test_orjsonl.jsonl', JSONL.encode('utf-8'))
    assert orjsonl.load(tmp_path / 'test_orjsonl.jsonl') == DATA


def test_stream(tmp_path) -> None:
    """Test `orjsonl.stream()`."""
    
    helpers.save(tmp_path / 'test_orjsonl.jsonl', JSONL.encode('utf-8'))
    assert list(orjsonl.stream(tmp_path / 'test_orjsonl.jsonl')) == DATA


def test_append(tmp_path) -> None:
    """Test `orjsonl.append()`."""
    
    helpers.save(tmp_path / 'test_orjsonl.jsonl', JSONL.encode('utf-8'))
    orjsonl.append(tmp_path / 'test_orjsonl.jsonl', data=DATA[-1])
    assert helpers.load(tmp_path / 'test_orjsonl.jsonl') == JSONL.encode('utf-8') + orjson.dumps(DATA[-1]) + b'\n'


def test_extend(tmp_path) -> None:
    """Test `orjsonl.extend()`."""

    helpers.save(tmp_path / 'test_orjsonl.jsonl', JSONL.encode('utf-8'))
    orjsonl.extend(tmp_path / 'test_orjsonl.jsonl', data=DATA[-2:])
    assert helpers.load(tmp_path / 'test_orjsonl.jsonl') == JSONL.encode('utf-8') + orjson.dumps(DATA[-2]) + b'\n' + orjson.dumps(DATA[-1]) + b'\n'
