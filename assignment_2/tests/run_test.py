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
    for i in range(len(indexes)-1):
        loops = len(range(indexes[i], indexes[i+1])) - 1
        if loops != 0:
            if loops in loops_runs_dic:
                loops_runs_dic[loops] += 1
            else:
                loops_runs_dic[loops] = 1
            if 1 in loops_runs_dic:
                loops_runs_dic[1] += 1
            else:
                loops_runs_dic[1] = 1
            if i+1 == len(indexes)-1:
                if 1 in loops_runs_dic:
                    loops_runs_dic[1] += 1
        # if numbers in indicies are consecutive
        else:
            fixed = i
            i += 1
            print("break the loop:")
            break
    print(sorted(loops_runs_dic.items(), key=lambda kv: kv[0]))
