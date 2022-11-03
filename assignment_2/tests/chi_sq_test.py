"""takes a list of generated random number"""


def chi_test(the_random_list):

    print("chi_test performed:")
    N = 10000
    _random = []
    _random = the_random_list
    E = 1000
    CHI_SQ_SIG_5_PERCENT_9_DEG = 16.92
    interval_1 = [0.0, 0.1]
    interval_2 = [0.1, 0.2]
    interval_3 = [0.2, 0.3]
    interval_4 = [0.3, 0.4]
    interval_5 = [0.4, 0.5]
    interval_6 = [0.5, 0.6]
    interval_7 = [0.6, 0.7]
    interval_8 = [0.7, 0.8]
    interval_9 = [0.8, 0.9]
    interval_10 = [0.9, 1.0]
    o_1 = 0
    o_2 = 0
    o_3 = 0
    o_4 = 0
    o_5 = 0
    o_6 = 0
    o_7 = 0
    o_8 = 0
    o_9 = 0
    o_10 = 0
    for i in range(1, N+1):
        if interval_1[0] <= _random[i-1] <= interval_1[1]:
            o_1 = o_1 + 1
        elif interval_2[0] <= _random[i-1] <= interval_2[1]:
            o_2 = o_2 + 1
        elif interval_3[0] <= _random[i-1] <= interval_3[1]:
            o_3 = o_3 + 1
        elif interval_4[0] <= _random[i-1] <= interval_4[1]:
            o_4 = o_4 + 1
        elif interval_5[0] <= _random[i-1] <= interval_5[1]:
            o_5 = o_5 + 1
        elif interval_6[0] <= _random[i-1] <= interval_6[1]:
            o_6 = o_6 + 1
        elif interval_7[0] <= _random[i-1] <= interval_7[1]:
            o_7 = o_7 + 1
        elif interval_8[0] <= _random[i-1] <= interval_8[1]:
            o_8 = o_8 + 1
        elif interval_9[0] <= _random[i-1] <= interval_9[1]:
            o_9 = o_9 + 1
        elif interval_10[0] <= _random[i-1] <= interval_10[1]:
            o_10 = o_10 + 1

    chi_list = [((o_1-E)**2)/E, ((o_2-E)**2)/E, ((o_3-E)**2)/E, ((o_4-E)**2)/E, ((o_5-E)**2)/E,
                ((o_6-E)**2)/E, ((o_7-E)**2)/E, ((o_8-E)**2)/E, ((o_9-E)**2)/E, ((o_10-E)**2)/E]
    chi_square_total = sum(chi_list)
    print(chi_square_total)
    if chi_square_total > CHI_SQ_SIG_5_PERCENT_9_DEG:
        print("H0 rejected")
    else:
        print("H0 is not rejected")
