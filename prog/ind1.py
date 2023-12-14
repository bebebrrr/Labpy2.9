#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def vec(arr):
    if len(arr) != 1:
        for i in arr:
            print(i, end = " ")
        print()


def find(arr, i, n):
    if n == 0:
        vec(arr)
    for j in range(i, n + 1):
        arr.append(j)
        find(arr, j, n - j)
        del arr[-1]


if __name__ == '__main__':
    n = 10
    arr = []
    find(arr, 1, n)
