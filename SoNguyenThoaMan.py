import random
import math

def square_loop(a, k, n):
    b = 1
    a %= n
    while k > 0:
        if k % 2 == 1:
            b = b*a % n
        k = k // 2
        a = pow(a, 2) % n
    return b



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

def main():
    k = 5
    a = int(input())
    b = int(input())
    if b < 0 or a > b or a < 0:
        print("NO")
        return
    primeCheck = [True] * (b - a + 1)
    for i in range(2 , round(math.sqrt(b)) + 1):
        for j in range(max(i*i,((a + i - 1) // i) * i), b + 1, i):
            primeCheck[j - a] = False
    if a <= 1:
        primeCheck[1 - a] = False
    sum = 0
    for i in range(a,b + 1):
        if primeCheck[i - a]:
            sum += i
    # print(sum)
    if isPrime(sum,k):
        print("YES")
    else:
        print("NO")
        


if __name__ == '__main__':
    main()
    