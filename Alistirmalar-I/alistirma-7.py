a=0
for i in range(100,999):
    if int(str(i)[0]) + int(str(i)[1]) == int(str(i)[2]):
        print(i)
        a+=1
print("Toplam {} sayi".format(a))
