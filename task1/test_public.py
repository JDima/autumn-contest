from typing import List

import pytest

from .task import task1


class Case:
    def __init__(self, name: str, n: int, conc: List[int], answer: int):
        self._name = name
        self.n = n
        self.conc = conc
        self.answer = answer

    def __str__(self) -> str:
        return 'task1_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        n=400,
        conc=[300, 100, 550, 600],
        answer=3
    ),
    Case(
        name='base2',
        n=50,
        conc=[125, 25],
        answer=4
    ),
    Case(
        name='base3',
        n=500,
        conc=[1000, 5, 5],
        answer=199
    ),
    Case(
        name='base4',
        n=500,
        conc=[1000],
        answer=-1
    ),
    Case(
        name='base5',
        n=874,
        conc=[873, 974, 875],
        answer=2
    ),
    Case(
        name='base6',
        n=999,
        conc=[1, 1000],
        answer=999
    ),
    Case(
        name='base7',
        n=500,
        conc=[996, 245, 884, 567, 913, 210, 389, 188, 389, 370,
              863, 613, 865, 990, 94, 536, 837, 518, 734, 471,
              644, 647, 36, 294, 755, 873, 911, 894, 981, 546,
              685, 180, 823, 233, 426, 161, 805, 13, 708, 864,
              524, 437, 596, 134, 967, 693, 320, 63, 567, 378,
              365, 384, 274, 383, 313, 49, 70, 601, 652, 75, 885,
              652, 843, 495, 279, 599, 711, 414, 625, 736, 386,
              737, 55, 708, 443, 617, 847, 561, 545, 830, 739,
              493, 504, 657, 671, 934, 192, 753, 37, 574, 806,
              384, 913, 312, 330, 735, 61, 191, 485, 250, 413,
              350, 566, 630, 764, 665, 451, 740, 119, 648, 444,
              765, 290, 302, 553, 412, 718, 827, 15, 462,
              646, 192, 676, 757, 662, 475, 729, 718],
        answer=2
    ),
    Case(
        name='base8',
        n=326,
        conc=[684, 49, 373, 57, 747, 132, 441, 385, 640, 575, 567, 665, 323, 515, 527, 656, 232, 701],
        answer=3
    ),
    Case(
        name='base9',
        n=314,
        conc=[160, 769, 201, 691, 358, 724, 248, 47, 420, 432, 667, 601, 596, 370, 469],
        answer=4
    ),
    Case(
        name='base10',
        n=0,
        conc=[0],
        answer=1
    ),
    Case(
        name='base11',
        n=0,
        conc=[1000],
        answer=-1
    ),
    Case(
        name='base12',
        n=345,
        conc=[497, 135, 21, 199, 873],
        answer=5
    ),
    Case(
        name='base13',
        n=641,
        conc=[807, 1000, 98, 794, 536, 845, 407, 331],
        answer=7
    ),
    Case(
        name='base14',
        n=852,
        conc=[668, 1000, 1000, 1000, 1000, 1000, 1000, 639, 213, 1000],
        answer=10
    ),
    Case(
        name='base15',
        n=710,
        conc=[854, 734, 63, 921, 921, 187, 978],
        answer=5
    ),
    Case(
        name='base16',
        n=134,
        conc=[505, 10, 1, 363, 344, 162],
        answer=4
    ),
    Case(
        name='base17',
        n=951,
        conc=[706, 1000, 987, 974, 974, 706, 792, 792, 974, 1000, 1000, 987, 974, 953, 953],
        answer=6
    ),
    Case(
        name='base18',
        n=834,
        conc=[921, 995, 1000, 285, 1000, 166, 1000, 999, 991, 983],
        answer=10
    ),
    Case(
        name='base19',
        n=917,
        conc=[999, 998, 1000, 997, 1000, 998, 78, 991, 964, 985, 987, 78, 985, 999, 83, 987, 1000, 999, 999, 78, 83],
        answer=12
    ),
    Case(
        name='base20',
        n=971,
        conc=[692, 1000, 1000, 997, 1000, 691, 996, 691, 1000, 1000, 1000, 692, 1000, 997, 1000],
        answer=11
    ),
    Case(
        name='base21',
        n=971,
        conc=[96, 706, 996, 984, 1000, 991, 996, 1000, 724, 724,
              997, 991, 997, 984, 997, 1000, 984, 996, 996, 997,
              724, 997, 997, 1000, 997, 724, 984, 997, 996, 988,
              997, 706, 706, 997, 1000, 991, 706, 988, 997, 724,
              988, 706, 996, 706, 724, 997, 988, 996, 991, 1000,
              1000, 724, 988, 996, 1000, 988, 984, 996, 991, 724,
              706, 988, 991, 724, 1000, 1000, 991, 984, 984, 706,
              724, 706, 988, 724, 984, 984, 991, 988, 991, 706,
              997, 984, 984, 1000, 706, 724, 988, 984, 996, 1000,
              988, 997, 984, 724, 991, 991],
        answer=10
    ),
    Case(
        name='base22',
        n=1000,
        conc=[536, 107, 113, 397, 613, 1, 535, 652, 730, 137, 239, 538, 764, 431, 613, 273],
        answer=-1
    ),
    Case(
        name='base23',
        n=998,
        conc=[1, 1000],
        answer=999
    ),
    Case(
        name='base24',
        n=998,
        conc=[1, 999, 1000],
        answer=500
    ),
    Case(
        name='base25',
        n=998,
        conc=[1, 2, 999, 1000],
        answer=499
    ),
    Case(
        name='base26',
        n=998,
        conc=[i for i in [0, 1000, 1, 1000, 999] for j in range(200_000)],
        answer=500
    ),
    Case(
        name='base27',
        n=999,
        conc=([1000] + [1 for _ in range(999_999)]),
        answer=999
    ),
    Case(
        name='base28',
        n=500,
        conc=[1000, 2],
        answer=499
    ),
    Case(
        name='base29',
        n=508,
        conc=[0, 998, 997, 1, 1, 2, 997, 1, 997, 1000, 0, 3, 3, 2, 4],
        answer=53
    ),
    Case(
        name='base30',
        n=492,
        conc=[706, 4],
        answer=351
    ),
    Case(
        name='base31',
        n=672,
        conc=[4, 6, 1000, 995, 997],
        answer=46
    ),
    Case(
        name='base32',
        n=410,
        conc=[998, 8, 990, 990],
        answer=54
    ),
    Case(
        name='base33',
        n=499,
        conc=[1000, 2],
        answer=998
    ),
    Case(
        name='base34',
        n=995,
        conc=[996, 997, 998, 999, 1000],
        answer=-1
    ),
    Case(
        name='base35',
        n=500,
        conc=[499, 1000, 300],
        answer=7
    ),
    Case(
        name='base36',
        n=499,
        conc=[0, 1000],
        answer=1000
    ),
    Case(
        name='base37',
        n=1000,
        conc=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        answer=-1
    ),
    Case(
        name='base38',
        n=501,
        conc=[1, 1000],
        answer=999
    )

]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task1(case: Case) -> None:
    answer = task1(
        n=case.n,
        conc=case.conc
    )
    assert answer == case.answer
