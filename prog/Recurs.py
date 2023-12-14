#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit


def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    

def fib(n):
   if n == 0 or n == 1:
       return n
   else:
       return fib(n - 2) + fib(n - 1)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    n = 10
    factorial(n)
    fib(n)
    print(f"Выполнение рекурсией: {(timeit.default_timer() - start_time):.12f}")