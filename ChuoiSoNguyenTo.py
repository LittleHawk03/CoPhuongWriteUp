import random


def square_loop(a, k, n):
    b = 1
    a %= n
    while k > 0:
        if k % 2 == 1:
            b = b*a % n
        k = k // 2
        a = pow(a, 2) % n
    return b


def miller(n):
    if (n <= 1 or n == 4):
        return False
    if (n <= 3):
        return True


def miillerTest(d, n):
    a = 2 + random.randint(1, n - 4)
    x = square_loop(a, d, n)
    if (x == 1 or x == n - 1):
        return True
    while (d != n - 1):
        x = (x * x) % n
        d *= 2

        if (x == 1):
            return False
        if (x == n - 1):
            return True

    return False


def isPrime(n, k):

    if (n <= 1 or n == 4):
        return False
    if (n <= 3):
        return True

    d = n - 1
    while (d % 2 == 0):
        d //= 2

    for i in range(k):
        if (miillerTest(d, n) == False):
            return False

    return True


def main(s):
    k = 4
    st = {}
    for i in range(len(s)):
        st[s[i]] = 0
    for i in range(len(s)):
        st[s[i]] += 1

    if not isPrime(len(st), k):
        return False

    for i in range(len(s)):
        if not isPrime(st[s[i]], k):
            return False
    return True


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = input()
        if main(n):
            print('YES')
        else:
            print('NO')
