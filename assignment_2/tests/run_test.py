"""Takes a random generated list of numbers"""


def run_test(the_random_list):
    """Run Test"""

    print("Run Test")

    _random = []
    _random = the_random_list
    largest = _random[0]
    plus_minus_list = []
    indexes = []
    loops_runs_dic = {
    }
    loops = 0
    counter = 0
    N = 10000
    no_plus_series = True

    for i in range(len(_random[1:])):
        if _random[i+1] > largest:
            largest = _random[i+1]
            plus_minus_list.append('+')
        else:
            plus_minus_list.append('-')

    for i in range(len(plus_minus_list)):
        if(plus_minus_list[i] == '+'):
            indexes.append(i)
    # print the indices for the + of the plus_minus_list
    print(indexes)

    # take in to account all the minuses before encountering the first + in indexes
    if indexes[0] != 0:
        if indexes[0] in loops_runs_dic:
            loops_runs_dic[indexes[0]] += 1
        else:
            loops_runs_dic[indexes[0]] = 1

    # take in to account all the minuses after encountering the last + in indexes
    if indexes[-1] != N-1:
        if N-1-indexes[-1] in loops_runs_dic:
            loops_runs_dic[N-1-indexes[-1]] += 1
        else:
            loops_runs_dic[N-1-indexes[-1]] = 1

    for i in range(len(indexes)-1):
        loops = len(range(indexes[i], indexes[i+1])) - 1
        if loops != 0:
            if loops in loops_runs_dic:
                loops_runs_dic[loops] += 1
            else:
                loops_runs_dic[loops] = 1
            # if we did not encounter + series we add just 1 period to the dic
            if no_plus_series is True:
                if 1 in loops_runs_dic:
                    loops_runs_dic[1] += 1
                else:
                    loops_runs_dic[1] = 1
            # when we reach to the end of the indexes list and we did not encounter + series we add 1 period to the dic
            if i+1 == len(indexes)-1:
                if 1 in loops_runs_dic:
                    loops_runs_dic[1] += 1
            no_plus_series = True
        # if numbers in indicies are consecutive
        else:
            j = i
            no_plus_series = False
            for _ in range(len(indexes)-1):
                if len(range(indexes[j], indexes[j+1])) - 1 == 0:
                    counter = len(range(indexes[j], indexes[j+1]))+1
                    j += 1
                else:
                    if counter in loops_runs_dic:
                        loops_runs_dic[counter] += 1
                    else:
                        loops_runs_dic[counter] = 1
                    break
            i = j
            j = 0
            counter = 0
    print(loops_runs_dic.items())
    # sorted version with respect to the length of period
    # print(sorted(loops_runs_dic.items(), key=lambda kv: kv[0]))
