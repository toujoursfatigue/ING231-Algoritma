x=[]
for i in range(1,350):
    if 120%i==200%i==350%i:
        x.append(i)
print(max(x))
