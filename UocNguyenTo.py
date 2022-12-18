import math

def main(n):
    isPrime = [True] * (n + 1)
    for i in range(2,round(math.sqrt(n)) + 1):
        if isPrime[i]:
            for j in range(i*i, n + 1, i):
                isPrime[j] = False
    
    countPrime = 0
    for i in range(2,n + 1):
        if isPrime[i] and (n % i == 0):
            countPrime += 1

    total = 1
    for i in range(2, n + 1):
        if isPrime[i]:
            count = 0
            if n % i == 0:
                while n % i == 0:
                    n = n // i
                    count += 1
            total = total * (count + 1)
    
    print(total)
    print(countPrime)
                
if __name__ == '__main__':
    n = int(input())
    main(n)
    