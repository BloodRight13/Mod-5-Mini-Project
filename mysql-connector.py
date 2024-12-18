import mysql.connector  
from mysql.connector import Error  
  
class Database:  
   def __init__(self, host, database, user, password):  
      self.host = host  
      self.database = database  
      self.user = user  
      self.password = password  
      self.connection = None  
  
   def connect(self):  
      try:  
        self.connection = mysql.connector.connect(  
           host=self.host,  
           database=self.database,  
           user=self.user,  
           password=self.password  
        )  
        print("Connected to the database")  
      except Error as e:  
        print(f"Error connecting to the database: {e}")  
  
   def disconnect(self):  
      if self.connection.is_connected():  
        self.connection.close()  
        print("Disconnected from the database")  
  
class Author:  
   def __init__(self, id, name, biography):  
      self.id = id  
      self.name = name  
      self.biography = biography  
  
class Book:  
   def __init__(self, id, title, author_id, isbn, publication_date, availability):  
      self.id = id  
      self.title = title  
      self.author_id = author_id  
      self.isbn = isbn  
      self.publication_date = publication_date  
      self.availability = availability  
  
class User:  
   def __init__(self, id, name, library_id):  
      self.id = id  
      self.name = name  
      self.library_id = library_id  
  
class LibraryManagementSystem:  
   def __init__(self, database):  
      self.database = database  
  
   def add_author(self, name, biography):  
      cursor = self.database.connection.cursor()  
      query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"  
      cursor.execute(query, (name, biography))  
      self.database.connection.commit()  
      cursor.close()  
  
   def add_book(self, title, author_id, isbn, publication_date):  
      cursor = self.database.connection.cursor()  
      query = "INSERT INTO books (title, author_id, isbn, publication_date) VALUES (%s, %s, %s, %s)"  
      cursor.execute(query, (title, author_id, isbn, publication_date))  
      self.database.connection.commit()  
      cursor.close()  
  
   def add_user(self, name, library_id):  
      cursor = self.database.connection.cursor()  
      query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"  
      cursor.execute(query, (name, library_id))  
      self.database.connection.commit()  
      cursor.close()  
  
   def borrow_book(self, user_id, book_id):  
      cursor = self.database.connection.cursor()  
      query = "INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, CURDATE())"  
      cursor.execute(query, (user_id, book_id))  
      self.database.connection.commit()  
      cursor.close()  
  
   def return_book(self, book_id):  
      cursor = self.database.connection.cursor()  
      query = "UPDATE borrowed_books SET return_date = CURDATE() WHERE book_id = %s"  
      cursor.execute(query, (book_id,))  
      self.database.connection.commit()  
      cursor.close()  
  
   def search_book(self, title):  
      cursor = self.database.connection.cursor()  
      query = "SELECT * FROM books WHERE title LIKE %s"  
      cursor.execute(query, (f"%{title}%",))  
      result = cursor.fetchall()  
      cursor.close()  
      return result  
  
   def display_all_books(self):  
      cursor = self.database.connection.cursor()  
      query = "SELECT * FROM books"  
      cursor.execute(query)  
      result = cursor.fetchall()  
      cursor.close()  
      return result  
  
   def display_all_users(self):  
      cursor = self.database.connection.cursor()  
      query = "SELECT * FROM users"  
      cursor.execute(query)  
      result = cursor.fetchall()  
      cursor.close()  
      return result  
  
   def display_all_authors(self):  
      cursor = self.database.connection.cursor()  
      query = "SELECT * FROM authors"  
      cursor.execute(query)  
      result = cursor.fetchall()  
      cursor.close()  
      return result