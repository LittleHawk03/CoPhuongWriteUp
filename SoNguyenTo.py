import math

def main(n):
    a = 10**(n-1)
    b = 10**n - 1
    isPrime = [True] * (b - a + 1)
    
    for i in range(2,round(math.sqrt(b)) + 1):
        for j in range(max(i*i,((a + i - 1) // i) * i), b + 1, i):
            isPrime[j - a] = False
    
    for i in range(a,b + 1):
        if isPrime[i - a]:
            print(float(i))
        
            

if __name__ == '__main__':
    n = int(input())
    main(n)
    