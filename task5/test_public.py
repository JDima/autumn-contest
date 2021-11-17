from typing import List

import pytest

from .task import task5


class Case:
    def __init__(self, name: str, n: int, m: int, ct: List[List[int]], answer: List[int]):
        self._name = name
        self.n = n
        self.m = m
        self.ct = ct
        self.answer = answer

    def __str__(self) -> str:
        return 'task5_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        n=5, m=6,
        ct=[[1, 2, 3],
            [2, 3, 4],
            [3, 4, 5],
            [4, 5, 6],
            [1, 5, 1],
            [2, 4, 2]],
        answer=[0, 98, 49, 25, 114],
    ),
    Case(
        name='base2',
        n=2, m=1,
        ct=[[2, 1, 48]],
        answer=[0, -1],
    ),
    Case(
        name='base3',
        n=10, m=20,
        ct=[[10, 1, 15],
            [7, 1, 32],
            [5, 3, 36],
            [3, 9, 14],
            [3, 4, 19],
            [6, 8, 4],
            [9, 6, 18],
            [7, 3, 38],
            [10, 7, 12],
            [7, 5, 29],
            [7, 6, 14],
            [6, 2, 40],
            [8, 9, 19],
            [7, 8, 11],
            [7, 4, 19],
            [2, 1, 38],
            [10, 9, 3],
            [6, 5, 50],
            [10, 3, 41],
            [1, 8, 3]],
        answer=[0, 2201, 779, 1138, 1898, 49, 196, 520, 324, 490],
    ),

]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task5(case: Case) -> None:
    answer = task5(
        n=case.n,
        m=case.m,
        ct=case.ct
    )
    assert answer == case.answer
