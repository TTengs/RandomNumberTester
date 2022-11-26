"""main file to run. It produces results whethers tests are rejected or not"""
import lcm_gen
import lcm_randu
import random_lib
from tests import ks_test
from tests import chi_sq_test
from tests import run_test

if __name__ == '__main__':
    """Run Test"""

    print("----A linear congruential generator---")
    run_test.run_test(lcm_gen.rn)

    print(" ")
    print("---RANDU generator---")
    run_test.run_test(lcm_randu.rando_list)

    print(" ")
    print("---python library generator---")
    run_test.run_test(random_lib.random_list)
