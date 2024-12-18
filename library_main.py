import mysql.connector  
from mysql.connector import Error
import _mysql_connector
def main():  
   database = database("localhost", "library", "root", "password")  
   database.connect()  
  
   lms = _mysql_connector(database)  
  
   while True:  
      print("Welcome to the Library Management System!")  
      print("1. Book Operations")  
      print("2. User Operations")  
      print("3. Author Operations")  
      print("4. Quit")  
  
      choice = input("Enter your choice: ")  
  
      if choice == "1":  
        book_operations(lms)  
      elif choice == "2":  
        user_operations(lms)  
      elif choice == "3":  
        author_operations(lms)  
      elif choice == "4":  
        break  
      else:  
        print("Invalid choice. Please try again.")  
  
def book_operations(lms):  
   while True:  
      print("Book Operations:")  
      print("1. Add a new book")  
      print("2. Borrow a book")  
      print("3. Return a book")  
      print("4. Search for a book")  
      print("5. Display all books")  
      print("6. Back to main menu")  
  
      choice = input("Enter your choice: ")  
  
      if choice == "1":  
        title = input("Enter book title: ")  
        author_id = int(input("Enter author ID: "))  
        isbn = input("Enter ISBN: ")  
        publication_date = input("Enter publication date (YYYY-MM-DD): ")  
        lms.add_book(title, author_id, isbn, publication_date)  
      elif choice == "2":  
        user_id = int(input("Enter user ID: "))  
        book_id = int(input("Enter book ID: "))  
        lms.borrow_book(user_id, book_id)  
      elif choice == "3":  
        book_id = int(input("Enter book ID: "))  
        lms.return_book(book_id)  
      elif choice == "4":  
        title = input("Enter book title: ")  
        result = lms.search_book(title)  
        for book in result:  
           print(book)  
      elif choice == "5":  
        result = lms.display_all_books()  
        for book in result:  
           print(book)  
      elif choice == "6":  
        break  
      else:  
        print("Invalid choice. Please try again.")  
  
def user_operations(lms):  
   while True:  
      print("User Operations:")  
      print("1. Add a new user")  
      print("2. View user details")  
      print("3. Display all users")  
      print("4. Back to main menu")  
  
      choice = input("Enter your choice: ")  
  
      if choice == "1":  
        name = input("Enter user name: ")  
        library_id = input("Enter library ID: ")  
        lms.add_user(name, library_id)  
      elif choice == "2":  
        user_id = int(input("Enter user ID: "))  
        # TODO: Implement view user details  
        pass  
      elif choice == "3":  
        result = lms.display_all_users()  
        for user in result:  
           print(user)  
      elif choice == "4":  
        break  
      else:  
        print("Invalid choice. Please try again.")  
  
def author_operations(lms):  
   while True:  
      print("Author Operations:")  
      print("1. Add a new author")  
      print("2. View author details")  
      print("3. Display all authors")  
      print("4. Back to main menu")  
  
      choice = input("Enter your choice: ")  
  
      if choice == "1":  
        name = input("Enter author name: ")  
        biography = input("Enter author biography: ")  
        lms.add_author(name, biography)  
      elif choice == "2":  
        author_id = int(input("Enter author ID: "))  
        # TODO: Implement view author details  
        pass  
      elif choice == "3":  
        result = lms.display_all_authors()  
        for author in result:  
           print(author)  
      elif choice == "4":  
        break  
      else:  
        print("Invalid choice. Please try again.")  
  
if __name__ == "__main__":  
   main()