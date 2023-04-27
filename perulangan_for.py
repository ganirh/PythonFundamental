"""
Program perulangan membaca buku
"""

bookStock = 43
print('Officer said: "Read all your book"')

bookRead = 0
print(f'Books has been read = {bookRead}')

for bookRead in range(1, bookStock+1):
    print(f"Books {bookRead} has been read")

print(f'Books has been read = {bookRead}')