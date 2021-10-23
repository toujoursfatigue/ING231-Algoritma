a=0
for i in range(10000,99999):
    if str(i)[0] == str(i)[1] and str(i)[3] == str(i)[4]:
        a+=1
print(a)
