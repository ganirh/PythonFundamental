"""
Program perulangan membaca buku sampai paham
"""
from typing import Any

bookStock = 23
print('Officer said: "Read all your book until you good"')

bookUnderstand = 0
readCount = 0
print(f'Books has been understood = {bookUnderstand}')

while readCount < bookStock * 2:
    readCount = readCount + 1

    if bookUnderstand == 10:
        print(f"Books {bookUnderstand + 1} has not understand")
    else:
        bookUnderstand = bookUnderstand + 1
        print(f"Books {bookUnderstand} has been read and understood")

if bookUnderstand == bookStock:
    print(f'Books has been understood = {bookUnderstand}')
else:
    print(f'Sorry, some book can not be understand. '
          f'There was only {bookUnderstand} can be good for me')