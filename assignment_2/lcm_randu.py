"""Takes 4 params and returns list of random integers in a list"""


def lcg_randu(modulus, _a_, _c_, seed):
    """RANDU"""
    i = 0
    rn_list = []
    while i < 10000:
        seed = (_a_ * seed + _c_) % modulus
        rn_list.append(seed/modulus)
        i = i + 1
    print(rn_list)


lcg_randu(pow(2, 31), 65539, 0, 123456789)
