import math

def gcd(a,b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

def phi(n):
    result = 1
    for i in range(2, n):
        if gcd(i,n) == 1:
            result += 1
    return result
        

def main():
    c = input().split()
    n = int(c[0])
    k = int(c[1])
    result = n
    while k > 0:
        result = phi(result)
        k -= 1
    print(result,end="")

if __name__ == '__main__':
    main()
    