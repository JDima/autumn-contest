from typing import List

import pytest

from .task import task4


class Case:
    def __init__(self, name: str, k: int, points: List[List[int]], answer: int):
        self._name = name
        self.k = k
        self.points = points
        self.answer = answer

    def __str__(self) -> str:
        return 'task4_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        k=1,
        points=[[1, 3], [2, 0], [5, 10], [6, -10]],
        answer=4
    ),
    Case(
        name='base2',
        k=3,
        points=[[0, 0], [3, 0], [9, 2]],
        answer=3,
    ),
    Case(
        name='base3',
        k=3,
        points=[[0, 0], [1, 3], [2, 0], [3, 0], [5, 10], [6, -10], [9, 2], [11, 10]],
        answer=14,
    )
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task4(case: Case) -> None:
    answer = task4(
        k=case.k,
        points=case.points,
    )
    assert answer == case.answer
