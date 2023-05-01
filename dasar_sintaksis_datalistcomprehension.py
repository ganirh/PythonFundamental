print('\nPerintah del')
daftar_buku = ['Switch On', 'the Innovators', 'Boundless Potential', 'Using Fuzzy Logic']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension')
daftar_buku = ['Switch On', 'the Innovators', 'Boundless Potential', 'Using Fuzzy Logic']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension dengan start')
daftar_buku = ['Switch On', 'the Innovators', 'Boundless Potential', 'Using Fuzzy Logic']
del daftar_buku[0:2]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension dengan start -')
daftar_buku = ['Switch On', 'the Innovators', 'Boundless Potential', 'Using Fuzzy Logic']
del daftar_buku[0:-2]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension dengan step')
daftar_buku = ['Switch On', 'the Innovators', 'Boundless Potential', 'Using Fuzzy Logic']
del daftar_buku[0::2]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
daftar_buku = ['Switch On', 'the Innovators', 'Boundless Potential', 'Using Fuzzy Logic']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
print('\nTampilkan list baru')
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nTampilkan list baru dengan comprehension; ganjil')
daftar_buku = ['1. Switch On', '2. the Innovators', '3. Boundless Potential', '4. Using Fuzzy Logic']
daftar_buku_baru = daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nTampilkan list baru dengan comprehension; genap')
daftar_buku = ['1. Switch On', '2. the Innovators', '3. Boundless Potential', '4. Using Fuzzy Logic']
daftar_buku_baru = daftar_buku[1::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nTampilkan list baru dengan comprehension; buang data di ujung')
daftar_buku = ['1. Switch On', '2. the Innovators', '3. Boundless Potential', '4. Using Fuzzy Logic']
daftar_buku_baru = daftar_buku[0:-1]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nTampilkan list baru dengan comprehension; buang data di ujung (genap)')
daftar_buku = ['1. Switch On', '2. the Innovators', '3. Boundless Potential', '4. Using Fuzzy Logic']
daftar_buku_baru = daftar_buku[0:-1:2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nTampilkan list baru dengan comprehension; ganjil')
daftar_buku = ['1. Switch On', '2. the Innovators', '3. Boundless Potential', '4. Using Fuzzy Logic']
daftar_buku_baru = daftar_buku[0::2]
print(daftar_buku[0::2])