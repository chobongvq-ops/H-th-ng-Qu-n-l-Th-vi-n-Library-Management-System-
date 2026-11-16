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
        """
        Nhiệm vụ của thành viên phụ trách: 
        Viết logic thêm sách mới vào danh sách self.books
        """
        pass

    def display_books(self):
        """Hiển thị danh sách sách có trong thư viện"""
        if not self.books:
            print("Thư viện hiện chưa có sách nào!")
        for b in self.books:
            print(f"ID: {b.book_id} | Tên: {b.title} | Tác giả: {b.author} | Số lượng: {b.quantity}")

# Khởi chạy chương trình mẫu
if __name__ == "__main__":
    library = LibrarySystem()
    print("=== HỆ THỐNG QUẢN LÝ THƯ VIỆN ĐÃ SẴN SÀNG ===")
