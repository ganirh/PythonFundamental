daftar_buku = ['Switch On', 'the Innovators', 'Boundless Potential']
print('Tampilkan variabel "daftar_buku"')
print(daftar_buku)

print('\nProses semua dengan for in')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi "daftar_buku" pada indeks tertentu')

print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampilkan dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = ['Switch On', 300, 'Adaptive Control', -322]
print('\nTampilkan dengan for in range, dimana tiap tipe data pada list berbeda - beda')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan nilai awal pada "awal_buku"')
daftar_buku = ['Switch On', 'the Innovators', 'Boundless Potential']
print('\nTambahkan 1 buku baru')
daftar_buku.append('Super Scalper')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nClear List')
daftar_buku.clear()
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti element pertama')
daftar_buku = ['Switch On', 'the Innovators', 'Boundless Potential']
daftar_buku[0] = 'Using Fuzzy Logic'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil Elemen ke-2')
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang diambil tadi adalah:')
print(buku)

print('\nPop')
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
        print(daftar_buku[i])

print('\nPop - 1')
daftar_buku = ['Switch On', 'the Innovators', 'Boundless Potential']
daftar_buku.pop(-1)
for i in range(0, len(daftar_buku)):
        print(daftar_buku[i])

print('\nPop - 2')
daftar_buku = ['Switch On', 'the Innovators', 'Boundless Potential']
daftar_buku.pop(-2)
for i in range(0, len(daftar_buku)):
        print(daftar_buku[i])

