from typing import List

import pytest

from .task import task2


class Case:
    def __init__(self, name: str, a: List[int], cross: List[int], answer: List[int]):
        self._name = name
        self.a = a
        self.cross = cross
        self.answer = answer

    def __str__(self) -> str:
        return 'task2_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        a=[1, 3, 2, 5],
        cross=[3, 4, 1, 2],
        answer=[5, 4, 3, 0],
    ),
    Case(
        name='base2',
        a=[1, 2, 3, 4, 5],
        cross=[4, 2, 3, 5, 1],
        answer=[6, 5, 5, 1, 0],
    ),
    Case(
        name='base3',
        a=[5, 5, 4, 4, 6, 6, 5, 5],
        cross=[5, 2, 8, 7, 1, 3, 4, 6],
        answer=[18, 16, 11, 8, 8, 6, 6, 0],
    ),
    Case(
        name='base4',
        a=[3, 3, 3, 5, 6, 9, 3, 1, 7, 3],
        cross=[3, 4, 6, 7, 5, 1, 10, 9, 2, 8],
        answer=[34, 29, 14, 11, 11, 11, 8, 3, 1, 0],
    ),
    Case(
        name='base5',
        a=[12, 9, 17, 5, 0, 6, 5, 1, 3, 1, 17, 17, 2, 14, 5, 1, 17],
        cross=[3, 7, 5, 8, 12, 9, 15, 13, 11, 14, 6, 16, 17, 1, 10, 2, 4],
        answer=[94, 78, 78, 77, 39, 39, 21, 21, 21, 21, 21, 21, 21, 9, 9, 5, 0],
    ),
    Case(
        name='base6',
        a=[1, 6, 9, 2, 10, 5, 15, 16, 17, 14, 17, 3, 9, 8, 12, 0, 2],
        cross=[9, 13, 15, 14, 16, 17, 11, 10, 12, 4, 6, 5, 7, 8, 2, 3, 1],
        answer=[65, 64, 64, 64, 64, 64, 64, 64, 64, 46, 31, 31, 16, 16, 9, 1, 0],
    ),
    Case(
        name='base7',
        a=[1 for i in range(100_000)],
        cross=[i for i in range(100_000)],
        answer=[100_000 - i for i in range(1, 100_001)],
    ),
    Case(
        name='base8',
        a=[1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],
        cross=[1, 2, 3, 4, 5, 6, 7],
        answer=[6000000000, 5000000000, 4000000000, 3000000000, 2000000000, 1000000000, 0],
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task2(case: Case) -> None:
    answer = task2(
        a=case.a,
        cross=case.cross,
    )
    assert answer == case.answer
