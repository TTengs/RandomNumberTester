"""Takes a random generated list of numbers"""
import math


def run_test(the_random_list):
    """Run Test"""

    print("Run Test")
    _random = []
    _random = the_random_list
    last_num = _random[0]
    plus_minus_list = []
    N = 10000

    for i in range(len(_random[1:])):
        if _random[i+1] > last_num:
            plus_minus_list.append('+')
        else:
            plus_minus_list.append('-')
        last_num = _random[i+1]
    # print(len(plus_minus_list))

    create_dictionary_of_runs(plus_minus_list, N)


def create_dictionary_of_runs(plus_minus_list, TOTAL_RANDOM_NUMBERS):
    """Create dictionary of length with each has number of runs"""

    plus_counter = 0
    minus_counter = 0
    loops_runs_dic = {}
    for i in range(0, len(plus_minus_list)):
        if(plus_minus_list[i] == '+'):
            plus_counter += 1
            if(plus_counter > 0 and minus_counter > 0):
                loops_runs_dic = append_to_dic(minus_counter, loops_runs_dic)
            minus_counter = 0
        else:
            minus_counter += 1
            if(minus_counter > 0 and plus_counter > 0):
                loops_runs_dic = append_to_dic(plus_counter, loops_runs_dic)
            plus_counter = 0

    sorted_list = sorted(loops_runs_dic.items(), key=lambda kv: kv[0])
    print(sorted_list)

    get_rule(sorted_list, TOTAL_RANDOM_NUMBERS)


def append_to_dic(c, loops_runs_dic):
    """ Create a dictionary with the length and number of runs"""

    runs_dic = loops_runs_dic
    if c in runs_dic:
        runs_dic[c] += 1
    else:
        runs_dic[c] = 1
    return runs_dic


def get_rule(sorted_list, N):
    rule_list = []
    # we have taken the first 6 and added them
    for i in range(0, 6):
        e = (2/(math.factorial(sorted_list[i][0]+3)))*(N*(sorted_list[i][0]**2 + 3*sorted_list[i][0] + 1) - (
            sorted_list[i][0]**3 + 3*sorted_list[i][0]**2 - sorted_list[i][0] - 4))
        o = sorted_list[i][1]
        # do not include in the list that gives division by zero
        # print("Expected: ", e)
        # print("Observed: ", o)
        if(e != 0):
            rule_list.append(math.pow(e-o, 2)/e)

    print("Summation is : ", sum(rule_list))
    k = 6
    df = k-1
    x = sum(rule_list)
    x_sigma = 11.07  # degree of freedom 5

    if(x > x_sigma):
        print("x > x_sigma", x, x_sigma)
        print("We reject the null hypothesis of independence")
    else:
        print("x < x_sigma", x, x_sigma)
        print("We do not reject the hypothesis of independence")
