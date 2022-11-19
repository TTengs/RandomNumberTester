"""takes a list of generated random number"""
import math


def k_s(the_random_list):

    print("ks_test performed:")
    N = 100

    d_plus = []

    d_minus = []

    _random = the_random_list

    # Rank the N random numbers
    _random.sort()

    # Calculate max(i/N-Ri)

    for i in range(1, N + 1):

        _x = i / N - _random[i-1]

        d_plus.append(_x)

    # Calculate max(Ri-((i-1)/N))

    for i in range(1, N + 1):

        _y = (i-1)/N

        _y = _random[i-1]-_y

        d_minus.append(_y)

    # Calculate max(D+, D-)

    D = max((max(d_plus)), (max(d_minus)))

    print("Value of D is :")

    print(D)
    if(D < 1.36/math.sqrt(N)):
        print("D < 1.36/SQRT(N)")
        print("*H0 is not rejected")
    else:
        print("D > 1.36/SQRT(N)")
        print("**H0 is rejected")
