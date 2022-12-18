import math

def solution(b):
    isPrime = [True] * (b + 1)
    if b < 0:
        return False
    
    isPrime[0] = False
    if b + 1 > 1:
        isPrime[1] = False
    count = 0
    for i in range(2, round(math.sqrt(b)) + 1):
        if isPrime[i]:
            for j in range(i * i, b + 1, i):
                isPrime[j] = False

    for i in range(2, b):
        if isPrime[i]:
            count += 1
            
    return isPrime[count]

def main():
    a = int(input())
    b = int(input())
    count = 0
    for i in range(a, b + 1):
        if solution(i):
            count += 1
    print(count)            
                                    

if __name__ == '__main__':
    main()
    