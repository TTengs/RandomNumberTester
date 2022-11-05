"""main file to run. It produces results whethers tests are rejected or not"""
import lcm_gen
import lcm_randu
import random_lib
from tests import ks_test
from tests import chi_sq_test
from tests import run_test

if __name__ == '__main__':
    """DO KS_TEST"""

    """ print("----A linear congruential generator---")
    ks_test.k_s(lcm_gen.rn[:100])
    print("---RANDU generator---")
    ks_test.k_s(lcm_randu.rando_list[:100])
    print("---python library generator---")
    ks_test.k_s(random_lib.random_list[:100]) """

    """DO CHI_SQUARE TEST"""

    """ print("----A linear congruential generator---")
    chi_sq_test.chi_test(lcm_gen.rn)
    print("---RANDU generator---")
    chi_sq_test.chi_test(lcm_randu.rando_list)
    print("---python library generator---")
    chi_sq_test.chi_test(random_lib.random_list) """

    print("----A linear congruential generator---")
    run_test.run_test(lcm_gen.rn)
    print("---RANDU generator---")
    run_test.run_test(lcm_randu.rando_list)
    print("---python library generator---")
    run_test.run_test(random_lib.random_list)
