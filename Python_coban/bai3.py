n = int(input())
en = 1 + (n-1)*2
for i in range(n):
    print(" "*i + "*"*(en-i*2) + " "*i)