import json
import time
from datetime import datetime

class PersonalLibraryManager:
    def __init__(self):
        self.books = []
        self.file_name = "library.json"
    
    def animate_text(self, text, delay=0.02):
        """Display text with animation effect."""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def display_header(self, title):
        """Display a formatted header."""
        print("\n" + "=" * 60)
        print(f"📚  {title.center(56)}  📚")
        print("=" * 60)
    
    def add_book(self):
        """Add a new book to the library."""
        self.display_header("ADD A NEW BOOK")
        
        title = input("📕 Enter title: ").strip()
        author = input("✍️  Enter author: ").strip()
        
        while True:
            try:
                year = int(input("📅 Enter publication year: ").strip())
                break
            except ValueError:
                print("❌ Invalid input! Please enter a valid year (number).")
        
        genre = input("🏷️  Enter genre: ").strip()
        read_input = input("👁️  Have you read this book? (y/n): ").strip().lower()
        read_status = read_input in ['y', 'yes']
        
        book = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read": read_status,
            "date_added": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.books.append(book)
        self.save_library()
        self.animate_text(f"\n✅ Book '{title}' by {author} added successfully! 🎉")
    
    def remove_book(self):
        """Remove a book from the library."""
        if not self.books:
            print("\n📭 Your library is empty. No books to remove.")
            return
        
        self.display_header("REMOVE A BOOK")
        title = input("🔍 Enter the title of the book to remove: ").strip()
        
        for i, book in enumerate(self.books):
            if book["title"].lower() == title.lower():
                removed_book = self.books.pop(i)
                self.save_library()
                self.animate_text(f"\n✅ Book '{removed_book['title']}' removed successfully! 🗑️")
                return
        
        print("\n❌ Book not found in your library!")
    
    def search_book(self):
        """Search for books by title or author."""
        if not self.books:
            print("\n📭 Your library is empty. No books to search.")
            return
        
        self.display_header("SEARCH FOR BOOKS")
        print("1. Search by Title")
        print("2. Search by Author")
        
        choice = input("\n👉 Enter your choice (1-2): ").strip()
        
        if choice == "1":
            field = "title"
            search_term = input("🔍 Enter title to search: ").strip().lower()
        elif choice == "2":
            field = "author"
            search_term = input("🔍 Enter author to search: ").strip().lower()
        else:
            print("\n❌ Invalid choice!")
            return
        
        found_books = [book for book in self.books if search_term in book[field].lower()]
        
        if found_books:
            self.display_header(f"SEARCH RESULTS ({len(found_books)} books found)")
            self._display_books(found_books)
        else:
            print(f"\n🔍 No books found matching your search.")
    
    def display_all_books(self):
        """Display all books in the library."""
        if not self.books:
            print("\n📭 Your library is empty.")
            return
        
        self.display_header(f"YOUR LIBRARY COLLECTION ({len(self.books)} books)")
        self._display_books(self.books)
    
    def _display_books(self, books_list):
        """Helper method to display a list of books."""
        for i, book in enumerate(books_list, 1):
            read_status = "✅ READ" if book["read"] else "⏳ UNREAD"
            print(f"{i}. 📘 {book['title']} ({book['year']})")
            print(f"   ✍️  Author: {book['author']}")
            print(f"   🏷️  Genre: {book['genre']}")
            print(f"   👁️  Status: {read_status}")
            print()
    
    def display_statistics(self):
        """Display library statistics."""
        if not self.books:
            print("\n📭 Your library is empty. No statistics available.")
            return
        
        total_books = len(self.books)
        read_books = sum(1 for book in self.books if book["read"])
        percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0
        
        genres = {}
        for book in self.books:
            genres[book["genre"]] = genres.get(book["genre"], 0) + 1
        
        self.display_header("LIBRARY STATISTICS")
        print(f"📚 Total number of books: {total_books}")
        print(f"📖 Books read: {read_books} ({percentage_read:.1f}%)")
        print(f"📖 Books unread: {total_books - read_books} ({100 - percentage_read:.1f}%)")
        
        if genres:
            print("\n📊 Books by genre:")
            for genre, count in sorted(genres.items(), key=lambda x: x[1], reverse=True):
                print(f"   🏷️  {genre}: {count}")
    
    def save_library(self):
        """Save the library to a JSON file."""
        try:
            with open(self.file_name, 'w') as file:
                json.dump(self.books, file, indent=4)
            return True
        except Exception as e:
            print(f"\n❌ Error saving library: {e}")
            return False
    
    def run(self):
        """Run the main program loop."""
        self.animate_text("\n✨ Welcome to Your Personal Library Manager! ✨", 0.03)
        
        while True:
            print("\n" + "-" * 60)
            print("📚 MAIN MENU 📚".center(60))
            print("-" * 60)
            print("1. 📕 Add a Book")
            print("2. 🗑️  Remove a Book")
            print("3. 🔍 Search for a Book")
            print("4. 📋 Display All Books")
            print("5. 📊 Display Statistics")
            print("6. 🚪 Exit")
            
            choice = input("\n👉 Enter your choice (1-6): ").strip()
            
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.remove_book()
            elif choice == "3":
                self.search_book()
            elif choice == "4":
                self.display_all_books()
            elif choice == "5":
                self.display_statistics()
            elif choice == "6":
                self.save_library()
                self.animate_text("\n💾 Library saved! Thank you for using Personal Library Manager! 👋", 0.03)
                break
            else:
                print("\n❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    library_manager = PersonalLibraryManager()
    library_manager.run()