Daftar = []

while True:
    nama = input ("Nama alat (ketik 'selesai' untuk berhenti): ")
    if nama == "selesai":
        break
    Daftar.append(nama)

print ()
print ("Daftar belanja: ")
for i, alat in enumerate (Daftar, start=1):
    print (f"{i} . {alat}")
print (f"Total: {len(Daftar)} alat")