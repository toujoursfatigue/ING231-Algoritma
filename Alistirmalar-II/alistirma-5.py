def asall(N):
    for i in range(2,N):
        if (N % i) == 0:
           return False
        else:
            return True

for i in range(10000,100000):
    if asall(i):
        if asall(int(str(i)[:-1])):
            if asall(int(str(i)[:-2])):
                if asall(int(str(i)[:-3])):
                    if asall(int(str(i)[:-4])):
                        print(i)
