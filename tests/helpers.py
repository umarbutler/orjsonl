from typing import Any

def save(path: str, data: Any) -> None:
    """Save a file."""
    
    with open(path, 'wb') as file:
        file.write(data)


def load(path: str) -> Any:
    """Load a file."""
    
    with open(path, 'rb') as file:
        return file.read()