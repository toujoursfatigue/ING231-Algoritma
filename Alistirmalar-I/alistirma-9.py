liste=[]
for i in range(100,999):
    if int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2]) < 9:
        liste.append(i)
print(liste)
