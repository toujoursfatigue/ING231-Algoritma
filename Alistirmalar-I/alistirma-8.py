a=0
for i in range(100,999):
    if str(i)[0] != str(i)[1] != str(i)[2]:
        continue
    else:
        a+=1
print(a)
