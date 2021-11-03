

def is_prime(n):
    for i in range(2,int(n**0.5 + 1)):
        if(n%i==0):
            return False 
    return True

if __name__ == "__main__":
    print("Nhập số n: ",end="")
    n = int(input())
    print(is_prime(n))