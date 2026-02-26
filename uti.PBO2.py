from datetime import date

class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"Buku '{self.title}' berhasil dipinjam.")
        else:
            print(f"Buku '{self.title}' sedang tidak tersedia.")

    def return_book(self):
        self.is_borrowed = False
        print(f"Buku '{self.title}' telah dikembalikan.")


class Staff:
    def __init__(self, name: str, staff_id: str):
        self.name = name
        self.staff_id = staff_id


class Member:
    def __init__(self, name: str, member_id: str):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = [] 
        
        
 # List untuk menyimpan objek BorrowTransaction

    def add_transaction(self, transaction):
        self.borrowed_books.append(transaction)


class BorrowTransaction:
    def __init__(self, book: Book, member: Member, staff: Staff):
        self.book = book
        self.member = member
        self.staff = staff
        self.borrow_date = str(date.today())
        self.returned = False

    def borrow_book(self, book: Book, staff: Staff):
        if not book.is_borrowed:
            book.borrow()
            self.returned = False
            print(f"Transaksi: {book.title} dipinjam oleh {self.member.name} (Petugas: {staff.name})")
        else:
            print("Gagal: Buku sudah dipinjam orang lain.")

    def return_book(self, book: Book, staff: Staff):
        book.return_book()
        self.returned = True
        print(f"Transaksi: {book.title} dikembalikan kepada {staff.name}")

# --- Contoh Penggunaan ---
# 1. Inisialisasi Objek
buku1 = Book("Pemrograman Python", "Guido van Rossum", "123-456")
anggota1 = Member("Budi", "M001")
petugas1 = Staff("Siti", "S001")

# 2. Melakukan Transaksi Peminjaman
transaksi1 = BorrowTransaction(buku1, anggota1, petugas1)
transaksi1.borrow_book(buku1, petugas1)
anggota1.add_transaction(transaksi1)

# 3. Melakukan Pengembalian
transaksi1.return_book(buku1, petugas1)
