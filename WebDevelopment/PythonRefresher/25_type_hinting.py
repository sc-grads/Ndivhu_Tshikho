from typing import List


def list_avg(sequence: list[int]) -> float:
    return sum(sequence) / len(sequence)

list_avg([1, 2, 3])