"""Random library that uses random function to generate random numbers between [0,1)"""
import random


def random_lib():
    """python random library"""
    i = 0
    rn_list = []
    while i < 10000:
        random_double = random.random()
        rn_list.append(random_double)
        i = i + 1
    return rn_list


random_list = random_lib()
