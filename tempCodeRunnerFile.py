import math
def checkChinhPhuong(n):
    i = int(math.sqrt(n))
    return i*i == n
def main():
    n = int(input())
    isPrime = [True] * (n + 1)
    for i in range(2,round(math.sqrt(n)) + 1):
        if isPrime[i]:
            for j in range(i*i,n + 1,i):
                isPrime[j] = False
            
    
    for i in range(2,n + 1):
        if checkChinhPhuong(i) and isPrime[int(math.sqrt(i))]:
            print(i)
if __name__ == '__main__':
    main()