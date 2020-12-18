# -*- coding: utf-8 -*-
from functools import reduce
from typing import List
import math


class Calc:
    def add(self, *args):
        return sum(args)

    def sub(self, a, b):
        return a - b

    def mul(self, *args):
        if not all(args):
            raise ValueError
        return reduce(lambda x, y: x * y, args)

    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "inf"

    def avg(self, iterable: List[float], ut: float = None, lt: float = None):

        if not iterable:
            return 0

        if not ut:
            ut = math.inf
        if not lt:
            lt = -math.inf

        filtered = [i for i in iterable if (lt <= i and i <= ut)]

        if not filtered:
            return 0

        return sum(filtered) / len(filtered)
