"""main file to run. It produces results whethers tests are rejected or not"""
import lcm_gen
import lcm_randu
import random_lib
# from tests import ks_test
# from tests import chi_sq_test
from tests import run_test
from tests import corollation_test

if __name__ == '__main__':

    print("----A linear congruential generator---")
    run_test.run_test(lcm_gen.rn)

    print(" ")
    print("---RANDU generator---")
    run_test.run_test(lcm_randu.rando_list)

    print("----A linear congruential generator---")
    run_test.run_test(lcm_gen.rn)

    print("")
    print("lcm generator without randu ")
    corollation_test.corollation_test(lcm_gen.rn)

    print(" ")
    print("lcm generator with randu ")
    corollation_test.corollation_test(lcm_randu.rando_list)

    print(" ")
    print("lcm generator using the library ")
    corollation_test.corollation_test(random_lib.random_list)
