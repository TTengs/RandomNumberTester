"""main file to run. It produces results whethers tests are rejected or not"""
import lcm_gen
import lcm_randu
import random_lib
from tests import ks_test
from tests import chi_sq_test
from tests import run_test
from tests import corollation_test

if __name__ == '__main__':

    print("----A linear congruential generator---")
    chi_sq_test.chi_test(lcm_gen.rn)

    print("")
    print("---RANDU generator---")
    chi_sq_test.chi_test(lcm_randu.rando_list)

    print("")
    print("---python library generator---")
    chi_sq_test.chi_test(random_lib.random_list)
