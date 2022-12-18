import math

def check(n):
    result = n
    for i in range(2 , int(math.sqrt(n)) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i;
            result -= result // i
    
    if n > 1:
        result -= result // n
    return result
def main():
    t = int(input())
    for i in range(t):
        a = int(input())
        print(check(a))
if __name__ == '__main__':
    main()