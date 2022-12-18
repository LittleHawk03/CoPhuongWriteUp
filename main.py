import math
def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or (n < 2):
        return False
    
    for i in range(2,round(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def main():
    n   = int(input())
    arr = [int(i) for i in input().split()]
    arr.sort()
    max = 0;
    min = 0;
    for i in range(n):
        if is_prime(arr[i]):
            min = arr[i];
            break;
    for i in range(n - 1, 0 , -1):
        if is_prime(arr[i]):
            max = arr[i];
            break;
    print(max - min)
        
    
    
if __name__ == '__main__':
    main()
    