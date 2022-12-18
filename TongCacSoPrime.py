import math
def main(a, b):
    is_Prime = [True] * (b - a + 1)

    sum = 0
    for i in range(2,round(math.sqrt(b)) + 1):
        for j in range(max(i*i , ((a + i - 1) // i) * i), b + 1, i):
            is_Prime[j - a] = False
    
    if a <= 1:
        is_Prime[1 - a] = False
    
    for i in range(a, b + 1):
        if is_Prime[i - a]:
            sum += i
    print(sum)            
        
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    main(a, b)
    