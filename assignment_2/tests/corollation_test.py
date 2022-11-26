"""Takes a random generated list of numbers"""
import math


def corollation_test(the_random_list):
    """corollation Test"""

    print("corollation_test")
    _random = []
    _random = the_random_list

    N = 10000
    i = 2
    m = 128

    # get M <= (N-i-m)/m
    M = get_M(N, i, m)
    rho = compute_rho(i, M, m, _random)
    print("rho is : ", rho)

    sigma = compute_sigma(M)
    print("sigma : ", sigma)

    Z = compute_Z(rho, sigma)
    print("Z is  : ", Z)
    
    isNotRejected = isHypothesisNotRejected(Z)
    if(isNotRejected):
        print("We do not reject the null hypothesis")
    else:
        print("We reject the null hypothesis")



def get_M(N, i, m):
    """calculat M from the given formula in the slides"""
    M = 0
    M = (N-i-m)/m
    print(int(M))
    return int(M)


def compute_rho(i, M, m, _random):
    k = 0
    the_list = []
    while k <= M:
        R1 = _random[i+(k*m)]
        R2 = _random[i+(k+1)*m]
        the_list.append(R1 * R2)
        k += 1
    the_list_sum = sum(the_list)
    return (the_list_sum / (M+1) - 0.25)


def compute_sigma(M):
    return (math.sqrt((13*M) + 7))/(12*(M+1))


def compute_Z(rho, sigma):
    return rho/sigma

def isHypothesisNotRejected(Z):
    notRejected = -1.96 < Z < 1.96
    return notRejected
