book = {}
num = int(input("Enter number of books: "))
for i in range(1, num+1):
    print(f"Please enter data of book {i}: ")
    title = input(f"Enter Title {i}: ")
    author = input(f"Enter Author {i}: ")
    gender = input(f"Enter Gener {i}: ")
    book[f"book{i}"] = {"Title" : title, "Author" : author, "Gender": gender}
print(book)
print(book["book1"]["Title"])