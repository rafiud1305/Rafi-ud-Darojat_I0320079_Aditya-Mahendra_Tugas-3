print ("#############################")
print ("Soal_Nomor_2")
print ("#############################")

Biodata = {'Nama' :["Rafi'ud Darojat"],
            'Hobi' :['Travelling', 'Nonton film', 'Berenang'],
            'Sosmed' :['@piud_ojat', 'Rafiud Darojat', 'Rafiud_13'],
            'Lagu' :['Into your arms', 'Bertaut', 'Alone 2'],
            'Makanan' :['Nasi goreng','Mie ayam','Ayam goreng']}

print ("Nama :",Biodata['Nama'])
print ("Hobi :",Biodata['Hobi'])
print ("Sosmed :",Biodata['Sosmed'])
print ("Lagu :",Biodata['Lagu'])
print ("Makanan:",Biodata['Makanan'])

print ("#############################")

Biodata['Hobi'][2] = 'Memanah'
Biodata['Sosmed'][1] = '@darojatrafiud'

print ("#############################")

del Biodata['Makanan'][2]
del Biodata['Makanan'][1]

print ("#############################")

Biodata['Hobi'].append("Main game")
print ("Nama :",Biodata['Nama'])
print ("Hobi :",Biodata['Hobi'])
print ("Sosmed :",Biodata['Sosmed'])
print ("Lagu :",Biodata['Lagu'])
print ("Makanan:",Biodata['Makanan'])


