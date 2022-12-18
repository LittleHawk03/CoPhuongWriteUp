import math

def main(a,b):
    isPrime = [True] * (b - a + 1)
    cout = 0
    for i in range(2,round(math.sqrt(b)) + 1):
        for j in range(max(i*i,((a + i - 1) // i) * i), b + 1, i):
            isPrime[j - a] = False
    if a <= 1:
        isPrime[1 - a] = False
    
    for i in range(a,b + 1):
        if isPrime[i - a]:
            cout += 1
    print(cout)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    main(a,b)
    