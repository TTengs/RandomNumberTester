"""Takes a random generated list of numbers"""
import math


def run_test(the_random_list):
    """Run Test"""

    print("Run Test")
    _random = []
    _random = the_random_list
    N = 10000

    loops_runs_dic = {}
    i = 0
    counter = 0

    while i < len(_random):
        if i == len(_random)-1:
            break
        if _random[i+1] > _random[i]:
            while _random[i+1] > _random[i]:
                counter += 1
                i += 1
                if i == len(_random)-1:
                    break
        else:
            while _random[i+1] < _random[i]:
                counter += 1
                i += 1
                if i == len(_random)-1:
                    break
        loops_runs_dic = append_to_dic(counter, loops_runs_dic)
        counter = 0
    sorted_list = sorted(loops_runs_dic.items(), key=lambda kv: kv[0])
    print(sorted_list)

    get_rule(sorted_list, N)


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
