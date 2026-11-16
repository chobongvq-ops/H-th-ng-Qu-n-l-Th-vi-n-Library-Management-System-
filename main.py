# ==========================================
# QUẢN LÝ THƯ VIỆN - HỆ THỐNG CƠ SỞ (BASE CODE)
# Trưởng nhóm khởi tạo để các thành viên cùng phát triển
# ==========================================

class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity

class LibrarySystem:
    def __init__(self):
        self.books = [] # Danh sách lưu trữ sách

    def add_book(self, book):
        # Kiểm tra mã sách đã tồn tại
        for b in self.books:
            if b.book_id == book.book_id:
                print("Mã sách đã tồn tại!")
                return False

        # Thêm sách vào danh sách
        self.books.append(book)
        print(f"Đã thêm sách: {book.title}")
        return True
    def display_books(self):
        if not self.books:
            print("Thư viện hiện chưa có sách nào!")
            return

        print("\n===== DANH SÁCH SÁCH =====")

        for b in self.books:
            print(f"Mã sách: {b.book_id}")
            print(f"Tên sách: {b.title}")
            print(f"Tác giả: {b.author}")
            print(f"Số lượng: {b.quantity}")
            print("------------------------")