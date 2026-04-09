import math

def hashFun(x):
    hash_val = (2 + 6 * x) % 32
    return hash_val

def trailingZeroes(n):
    if n == 0:
        return 32
    count = 0
    while (n & 1) == 0:
        count += 1
        n >>= 1
    return count

def main():
    vec = [1, 2, 2, 3, 4, 6, 2, 8, 3, 10, 14]
    R = 0
    
    for x in vec:
        h = hashFun(x)
        tz = trailingZeroes(h)
        R = max(R, tz)
    
    estimate = int(math.pow(2, R))
    print("Estimated number of distinct elements:", estimate)

if __name__ == "__main__":
    main()