import math

def countOfDivisior(n):
    isPrime = [True] * (n + 1)
    for i in range(2, round(math.sqrt(n)) + 1):
         if isPrime[i]:
             for j in range(i*i , n + 1, i):
                 isPrime[j] = False
    
    total = 1
    for i in range(2,n + 1):
        if isPrime[i]:
            count = 0
            if n % i == 0:
                while n % i == 0:
                    n = n // i
                    count += 1
            total = total * (count + 1)
    return total == 3
    

def main():
    n = int(input())
    for i in range(n + 1):
        if countOfDivisior(i):
            print(i)

    
if __name__ == '__main__':
    main()
    