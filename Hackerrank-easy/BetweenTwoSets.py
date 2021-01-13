# Source : https://www.hackerrank.com/challenges/between-two-sets/problem

def getTotalX(a, b):
    count = 0
    def lcm(a, b):
        return (a*b)//math.gcd(a,b)
    if len(a) == 1:
        LCM = a[0]
    else:
        LCM = lcm(a[0], a[1])
        for i in range(2,len(a)):
            LCM = lcm(a[i], LCM)
    if len(b) == 1:
        HCF = b[0]
    else:
        HCF = math.gcd(b[0], b[1])
        for i in range(2,len(b)):
            HCF = math.gcd(HCF, b[i])
    for i in range(LCM, HCF+1, LCM):
        if i%LCM == 0 and HCF%i == 0:
            count += 1
    return count
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
