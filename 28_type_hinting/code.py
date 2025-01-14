# Type hinting is a Python's 3.5 feature

from typing import List

def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)

# Works with a Python linter
# Linter will warn you if you pass a incorrect type as a parameter
list_avg(123)

class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        