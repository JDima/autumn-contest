from typing import List

import pytest

from .task import task3


class Case:
    def __init__(self, name: str, points: List[List[int]], answer: int):
        self._name = name
        self.points = points
        self.answer = answer

    def __str__(self) -> str:
        return 'task3_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        points=[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]],
        answer=20
    ),
    Case(
        name='base2',
        points=[[3, 12], [-2, 5], [-4, 1]],
        answer=18,
    ),
    Case(
        name='base3',
        points=[[0, 0], [1, 1], [1, 0], [-1, 1]],
        answer=4,
    ),
    Case(
        name='base4',
        points=[[-1000000, -1000000], [1000000, 1000000]],
        answer=4000000,
    ),
    Case(
        name='base5',
        points=[[0, 0]],
        answer=0,
    ),
    Case(
        name='base6',
        points=[[-1000000, -1000000],
                [-1000000, 1000000],
                [0, 0],
                [1000000, -1000000],
                [1000000, 1000000]],
        answer=8000000,
    ),
    Case(
        name='base7',
        points=[[480250, -169685],
                [-929175, -252944],
                [914431, -992332],
                [-167828, 41821],
                [222805, 901706],
                [799081, 523745],
                [-185958, -40812],
                [-231339, 786633],
                [-791200, 371184],
                [289159, -29290],
                [218101, 301636],
                [713115, 449498],
                [474873, -428838],
                [1054, 824886],
                [-845517, 970595],
                [-363470, 703373],
                [-400162, 509042],
                [-988573, -415705],
                [769921, -369863],
                [309378, 36081]],
        answer=7333529,
    ),

]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task3(case: Case) -> None:
    answer = task3(
        points=case.points,
    )
    assert answer == case.answer
