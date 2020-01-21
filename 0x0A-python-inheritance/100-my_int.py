#!/usr/bin/python3
"""Task 12 My integer."""


class MyInt(int):
    """A class (MyInt) that inherits from int."""

    def __eq__(self, value):
        """Inverts == to !=."""
        return super().__ne__(value)

    def __ne__(self, value):
        """Inverts != to ==."""
        return super().__eq__(value)
