def fibo(N):
    if N==1:
        return 0
    elif N==2:
        return 1
    else:
        return fibo(N-1) + fibo(N-2)

for i in range(1,31):
    print(fibo(i),end=" ")
