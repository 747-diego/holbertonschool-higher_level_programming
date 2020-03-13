#!/usr/bin/python3
"""Pascal's Triangle."""


def pascal_triangle(n):
    """Return a lists of integers representing the Pascal’s triangle."""
    PasTri = []
    for TriangleNum in range(1, n + 1):
        PasTri.append([1] * TriangleNum)

    for idx1 in range(2, n):
        TriPosition = PasTri[idx1]
        TriPosBack = PasTri[idx1 - 1]

        for idx2 in range(1, len(TriPosition) - 1):
            TriPosition[idx2] = TriPosBack[idx2 - 1] + TriPosBack[idx2]
    return PasTri
