# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 15:45:40 2026

@author: itsom
"""

def power(base, exp):
    result = base ** exp
    return result


def average(numbers_list):
    total = sum(numbers_list)
    count = len(numbers_list)
    avg = total / count
    return avg
    