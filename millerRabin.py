import random

def is_Prime(x,k):
    if x == 0 or x == 1 or x == 4 or x == 6 or x == 8 or x == 9:
        return False
    if x == 2 or x == 3 or x == 5 or x == 7:
        return True
    # phân tích n-1 = 2^s*r
    s = 0
    r = x - 1
    while r % 2 == 0:
        r >>= 1
        s += 1
    assert (2 ** s * r == x - 1)

    def trial_composite(a):
        if pow(a, r, x) == 1:  # a^r mod n == 1
            return False
        for j in range(s):
            if pow(a, 2 ** j * r, x) == x - 1:  # a^(2jr) mod n = -1
                return False
        return True

    for i in range(k):
        a = random.randrange(2, x-2)
        if trial_composite(a):
            return False

    return True


def check_number_is_prime(x,k):
    if is_Prime(x,k):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    check_number_is_prime(n,k)
