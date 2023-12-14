#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
from functools import lru_cache


@lru_cache
def fib(n):
    if n == 0 or n == 1:
       return n
    else:
       return fib(n - 2) + fib(n - 1)


@lru_cache
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    n = 10
    fib(n)
    factorial(n)
    print(f"Выполнение с декоратором: {(timeit.default_timer() - start_time):.12f}")