myLibrary = []

def add_book():
    print("\nEnter book details:")
    title = input("Title: ")
    author = input("Author: ")
    year = input("Year of Publication: ")
    genre = input("Genre: ")
    status = input("Have you read this book? (yes/no): ").lower()

    read = True if status == "yes" else False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }

    myLibrary.append(book)
    print("✅ Book added successfully!\n")

def remove_book():
    title = input("Enter the title of the book to remove: ")
    for book in myLibrary:
        if book["title"].lower() == title.lower():
            myLibrary.remove(book)
            print("✅ Book removed.\n")
            return
    print("❌ Book not found.\n")

def search_books():
    keyword = input("Enter title/author/genre to search: ").lower()
    found = [book for book in myLibrary if
             keyword in book["title"].lower() or
             keyword in book["author"].lower() or
             keyword in book["genre"].lower()]
    if found:
        print("\n📚 Found books:")
        for book in found:
            read_status = "Read" if book["read"] else "Unread"
            print(f"- {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    else:
        print("❌ No books matched your search.\n")

def display_all_books():
    if not myLibrary:
        print("\n📭 Your Library is empty.\n")
        return

    print("\n📚 Your Library:")
    for i, book in enumerate(myLibrary, 1):
        read_status = "Read" if book["read"] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")

def display_statistics():
    total = len(myLibrary)
    read_count = sum(1 for book in myLibrary if book["read"])
    percentage = (read_count / total) * 100 if total > 0 else 0

    print(f"\n📊 Total books: {total}")
    print(f"📈 Percentage read: {percentage:.1f}%\n")

def menu():
    while True:
        print("\n📘 Personal Library Menu")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Books")
        print("4. View All Books")
        print("5. View Statistics")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            search_books()
        elif choice == '4':
            display_all_books()
        elif choice == '5':
            display_statistics()
        elif choice == '6':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# Start the program
menu()




