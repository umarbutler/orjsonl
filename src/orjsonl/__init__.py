"""A simple, fast and lightweight Python library for loading, saving, streaming and appending both compressed and uncompressed jsonl (also known as ‘json lines’, ‘newline-delimited json’ and ‘ndjson’) files."""

from .orjsonl import (
    stream,
    load,
    save,
    append
)
