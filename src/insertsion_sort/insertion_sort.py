class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
    def __str__(self):
        return f'{self.title}'
def insertion_sort_by_book_title(arr_of_books):
    # iterate through the entire array, skip the first element
    for i in range(1, len(arr_of_books)):
        curr_book = arr_of_books[i]
        book_index = i
        while book_index > 0 and curr_book.title < arr_of_books[book_index-1].title:
            arr_of_books[book_index], arr_of_books[book_index - 1] = arr_of_books[book_index-1], arr_of_books[book_index]
            book_index -= 1

arr_of_books = [
    Book("Harry Potter and the Sorcerer's Stone", "JK Rowling", "Children's Fantasy"),
    Book("A Game of Thrones", "George RR Martin", "Adult Fantasy"),
    Book("Show Your Work", "Austin Kleon", "Self Help"),
    Book("The Lord of the Rings: The Fellowship of the Ring", "JRR Tolkien", "High Fantasy"),
    Book("Clean Code", "Robert J Martin", "Programming"),
    Book("The Rust Programming Language", "Steve Klabnik and Carol Nichols", "Programming"),
    Book("The Way of Kings", "Brandon Sanderson", "High Fantasy")
]

insertion_sort_by_book_title(arr_of_books)
for book in arr_of_books:
    print(book)
