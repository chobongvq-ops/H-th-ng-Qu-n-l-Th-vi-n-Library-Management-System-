import unittest
from main import LibrarySystem, Book

class TestLibrary(unittest.TestCase):
    def test_add_book_success(self):
        lib = LibrarySystem()
        book = Book("B01", "Python Cơ Bản", "Nguyen Van A", 5)
        result = lib.add_book(book)
        self.assertTrue(result)
        self.assertEqual(len(lib.books), 1)

if __name__ == '__main__':
    unittest.main().
