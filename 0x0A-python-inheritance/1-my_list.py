#!/usr/bin/python3
"""Task 1 My list."""


class MyList(list):
    """A class MyList that inherits from list."""

    def print_sorted(self):
        """Public instance method that prints a sorted list."""
        print(sorted(self))
