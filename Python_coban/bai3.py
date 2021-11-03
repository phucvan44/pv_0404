if __name__ == "__main__":
    print("Nhập số n: ",end="")
    n = int(input())

    lim = 1 + (n-1)*2

    for i in range(n):
        print(" "*i + "*"*(lim-i*2) + " "*i)