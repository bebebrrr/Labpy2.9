#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import timeit


def factorial(n):
    product = 1
    while n > 1:
       product *= n
       n -= 1
    return product


def fib(n):
    a, b = 0, 1
    while n > 0:
       a, b = b, a + b
       n -= 1
    return a


if __name__ == '__main__':
    start_time = timeit.default_timer()
    n = 10
    factorial(n)
    fib(n)
    print(f"{(timeit.default_timer() - start_time):.12f}")
    