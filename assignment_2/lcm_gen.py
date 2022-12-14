"""Takes 4 params and returns list of random integers in a list"""


def lcg(modulus, _a_, _c_, seed):
    """A linear congruential generator"""

    i = 0
    rn_list = []
    while i < 10000:
        seed = (_a_ * seed + _c_) % modulus
        rn_list.append(seed/modulus)
        i = i + 1
    return rn_list


rn = lcg(pow(2, 16), 101427, 321, 123456789)
