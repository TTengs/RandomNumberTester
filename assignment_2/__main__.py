"""main file to run. It produces results whethers tests are rejected or not"""
import lcm_gen
import lcm_randu
import random_lib
from tests import ks_test

if __name__ == '__main__':

    print("----A linear congruential generator---")
    ks_test.k_s(lcm_gen.rn[:100])

    print(" ")
    print("---RANDU generator---")
    ks_test.k_s(lcm_randu.rando_list[:100])

    print(" ")
    print("---python library generator---")
    ks_test.k_s(random_lib.random_list[:100])
