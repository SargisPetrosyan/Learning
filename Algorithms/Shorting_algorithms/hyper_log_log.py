"""
hyperloglog.py

A Python implementation of the HyperLogLog algorithm for approximate cardinality estimation.

The HyperLogLog algorithm is a probabilistic data structure used to estimate the number of distinct elements 
in a multiset (the cardinality) using fixed memory. It is particularly useful for processing large data streams 
where exact counting is computationally expensive or infeasible.
"""

from typing import Generator
import random

def random_nums_list(start:int, end:int) -> list[int]:
    '''generating random mails'''
    random_nums_list:list[int] = []
    iteration:int = 0
    while iteration < 100_000 :
        rand_num:int = random.randint(start,end)
        while rand_num in random_nums_list:
            rand_num:int = random.randint(start,end)
        random_nums_list.append(rand_num)
        iteration += 1
    return random_nums_list
    
def hyper_log_log(elements:list[int]) -> int:
    '''Hyper-log-log checking unique elements'''
    aprox_unique:int = 0
    for element in elements:
        num_bin = str(bin(element))
        while num_bin[-1] == 0:
            num_bin.removesuffix()
            aprox_unique += 0

def


