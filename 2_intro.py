#perulangan

# contoh1 
i = 0
for i  in range (10):
    print (i)

#contoh2
i = 1
for i in range (10):
    i += 1
    print (i)

#contoh3
i = 0
for baris in range (5):
    for kolom in range (5):
        print ("*", end="")
    print()

#contoh4
i = 0
for baris  in range (5):
    for kolom in range (5):
        print ("*")
    print ()

#contoh5 ( untuk mengehentikan pakai  ctrl + c)
#while iteration -> Need condition (lakukan perulangan saat i < 10)
baris2 = 0
while baris2 < 5:
    kolom2 = 0
    while kolom2 < 5 :
        print ("*", end = "")
  print ()

#contoh6 ( yang bisa berhenti)
baris2 = 0
while baris2 < 5 :
    baris2 +=1
    kolom2 = 0
    while kolom2 < 5 :
        kolom2 +=1
        print("*", end = "")
 print()

#contoh7
baris2 = 0
tengah = 5
while baris2 < 5:
    kolom2 = 0
    if(baris2 % 2 == 1 ):
        while kolom2 <5:
            if(kolom2 == int(round(tengah/2))):
                print("*", end="")
            else:
                print(" ", end="")
            kolom2 +=1
    else:
        while kolom2 <5 :
            print ("*", end="")
            kolom2 += 1
    print()
    baris2 += 1        


