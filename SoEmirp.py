import random

def rever(n):
    x = 0
    while n > 0:
        x = (x * 10) + n % 10
        n = n // 10
    return x

def square_loop(a,k,n):
    b = 1
    a %= n
    while k > 0:
        if k % 2 == 1:
            b = (b * a) % n
        k = k // 2
        a = (a**2) % n
    return b    

def miller(r,n):
    a = 2 + random.randint(1 , n - 4)
    x = square_loop(a,r,n)
    if x == 1 or x == n - 1:
        return True
    while (r != n - 1):
        x = (x*x) % n
        r *= 2
        if x == 1:
            return False
        if x == n - 1:
            return True
    return False
            
def isPrime(n,k):
    if (n <= 1 or n == 4):
        return False
    if (n <= 3):
        return True
    r = n - 1
    while (r % 2 == 0):
        r = r // 2
    
    for i in range(k):
        if miller(r,n) == False:
            return False
    return True
                
def main():
    n = int(input())
    k = 4
    if n > 2:
        print(2)
        
    for i in range(3,n,2):
        if isPrime(i,k) and isPrime(rever(i),k):
            print(i)
            

if __name__ == '__main__':
    main()
    