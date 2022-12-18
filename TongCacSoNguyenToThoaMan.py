import math
def main(n):
    
    isPrime = [True] * (n + 1)
    for i in range(2,round(math.sqrt(n)) + 1):
        if isPrime[i]:
            for j in range(i*i , n + 1, i):
                isPrime[j] = False
    sum = 0
    for i in range(2,n + 1):
        if isPrime[i]:
            sum += i
    print(sum)        
if __name__ == '__main__':
    n = int(input())
    main(n)
    