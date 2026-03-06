class Book:
    def __init__(self, book_id, title, author, price, copies_available):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price
        self.copies_available = copies_available

    def display_book(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Copies Available:", self.copies_available)
        print()

    def issue_book(self, quantity):
        if quantity > self.copies_available:
            print("Not enough copies available")
        else:
            self.copies_available -= quantity
            print(quantity, "copies issued")

    def add_copies(self, quantity):
        self.copies_available += quantity
        print(quantity, "copies added")

    def book_value(self):
        return self.price * self.copies_available


library = [
    Book(101, "Python Programming", "Mark Lutz", 750, 5),
    Book(102, "Data Structures and Algorithms", "Thomas H. Cormen", 1200, 3),
    Book(103, "Machine Learning Basics", "Andrew Ng", 950, 4)
]

print("Library Books\n")
for book in library:
    book.display_book()

library[0].issue_book(2)

library[2].add_copies(3)

total_value = 0
for book in library:
    total_value += book.book_value()

print("\nTotal value of all books in library:", total_value)
