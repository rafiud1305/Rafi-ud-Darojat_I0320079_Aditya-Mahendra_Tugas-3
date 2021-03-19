print ("#############################")
print ("Soal_Nomor_1")
print ("#############################")

Nama_Sahabat = ["Alam","Anan","Ilham","Fazri","Fahmi","Imam","Mn","Chairul","Fahri","Nurki"]
print(Nama_Sahabat)

print ("=====================================")

print ("Nama sahabat ke 4 :",Nama_Sahabat [4])
print ("Nama sahabat ke 5 :",Nama_Sahabat [6])
print ("Nama sahabat ke 6 :",Nama_Sahabat [7])

print ("=====================================")

Nama_Sahabat[3] = "Darul"
print ("Nama sahabat ke 3 :", Nama_Sahabat [3])
Nama_Sahabat[5] = "Dedi"
print ("Nama sahabat ke 5 :", Nama_Sahabat [5])
Nama_Sahabat[9] = "Miqdad"
print ("Nama sahabat ke 9 :", Nama_Sahabat [9])

print ("=====================================")

Nama_Sahabat.append("Ridwan")
print(Nama_Sahabat)
Nama_Sahabat.append("Ghoni")
print(Nama_Sahabat)

print ("=====================================")

for nama in Nama_Sahabat:
    print(nama)

print ("=====================================")

print(len(Nama_Sahabat))