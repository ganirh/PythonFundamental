"""
Program perulangan membaca buku
"""

bookStock = 23
print('Officer said: "Read all your book"')

bookRead = 0
print(f'Books has been read = {bookRead}')

while bookRead < bookStock:
    bookRead = bookRead + 1
    print(f"Books {bookRead} has been read")

print(f'Books has been read = {bookRead}')