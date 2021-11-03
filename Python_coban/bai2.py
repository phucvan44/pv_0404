def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)


def lcm(a,b):
    return a*b/gcd(a,b)


if __name__ == "__main__":
    print("Nhập số a: ",end="")
    n = int(input())

    print("Nhập số b: ",end="")
    m = int(input())

    print(int(lcm(n,m)))
    