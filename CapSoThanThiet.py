import math

def sumOfDivior(n):
    sum = 1;
    for i in range(2, round(math.sqrt(n)) + 1):
        if n % i == 0:
            if (n / i) == i:
                sum += i
            else:
                sum += (i + (n // i))
    return sum

def main(n):
    for i in range(1, n + 1):
        a = sumOfDivior(i)
        if (i == sumOfDivior(a)) and a != i and a < n and i < a:
            print(i,end=" ")
            print(a)
               
           

if __name__ == '__main__':
    n = int(input())
    main(n)
    