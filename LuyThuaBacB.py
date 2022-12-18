import math
p = 1000000007
def square_loop2(a, k):
    b = 1
    a %= p
    while k > 0:
        if k % 2 == 1:
            b = b*a % p
        k = math.floor(k/2)
        a = pow(a, 2) % p
    return b

def main():
    a = int(input())
    b = int(input())
    print(square_loop2(a,b))

if __name__ == '__main__':
    main()
    