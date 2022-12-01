"""main file to run. It produces results whethers tests are rejected or not"""
import lcm_gen
import lcm_randu
import random_lib
from tests import ks_test
from tests import chi_sq_test
from tests import run_test
from tests import corollation_test

if __name__ == '__main__':

    """corolation Test"""

    print("----A linear congruential generator---")
    corollation_test.corollation_test(lcm_gen.rn)

    print("")
    print("---RANDU generator---")
    corollation_test.corollation_test(lcm_randu.rando_list)

    print("")
    print("---python library generator---")
    corollation_test.corollation_test(random_lib.random_list)

    print("######## End of corolation Test #########")

    """Run Test"""
    print("----A linear congruential generator---")
    run_test.run_test(lcm_gen.rn)

    print("")
    print("---RANDU generator---")
    run_test.run_test(lcm_randu.rando_list)

    print("")
    print("---python library generator---")
    run_test.run_test(random_lib.random_list)

    print("######## End of Run Test #########")

    """chiSquare Test"""

    print("----A linear congruential generator---")
    chi_sq_test.chi_test(lcm_gen.rn)

    print("")
    print("---RANDU generator---")
    chi_sq_test.chi_test(lcm_randu.rando_list)

    print("")
    print("---python library generator---")
    chi_sq_test.chi_test(random_lib.random_list)

    print("######## End of chiSquare Test #########")

    """ks Test"""

    print("----A linear congruential generator---")
    ks_test.k_s(lcm_gen.rn)

    print("")
    print("---RANDU generator---")
    ks_test.k_s(lcm_randu.rando_list)

    print("")
    print("---python library generator---")
    ks_test.k_s(random_lib.random_list)

    print("######## End of ks Test #########")
