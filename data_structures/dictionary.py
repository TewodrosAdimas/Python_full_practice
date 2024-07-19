books_num = int(input("How many books do you want to add? "))
fav_books = {}

for i in range(1, books_num + 1):

    book_title = input(f"Enter title {i}: ")
    book_author = input(f"Enter author {i}: ")
    book_genre = input(f"Enter genre {i}: ")
    fav_books[f"title {i}"] = book_title
    fav_books[f"author {i}"] = book_author
    fav_books[f"genre {i}"] = book_genre

print(fav_books)
print(len(fav_books))