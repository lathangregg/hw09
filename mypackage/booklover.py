import numpy as np
import pandas as pd

class BookLover:

    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        if type(name) != str:
            raise TypeError("Name must be string type")
        if type(email) != str:
            raise TypeError("Email must be a string")
        if type(fav_genre) != str:
            raise TypeError("Favorite genre must be equal to a string")
        if type(num_books) != int:
            raise TypeError("Number of books must be an integer")
        if type(book_list) != pd.core.frame.DataFrame:
            raise TypeError("Book list must be a Pandas DataFrame")
        if book_list.columns[0] != 'book_name' or book_list.columns[1] != 'book_rating':
            raise ValueError("The column names for the book list must be book_name and book_rating")
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list

    def add_book(self,book_name,rating):
        if type(book_name) != str:
            raise TypeError(f"book name must be a string")
        if type(rating) != int:
            raise TypeError(f"rating must be an integer value")
        if rating not in range(0,6):
            raise ValueError("rating must be a value between 0 and 5")
        if book_name not in list(self.book_list['book_name']):
            new_book = pd.DataFrame({
                'book_name': [book_name],
                'book_rating': [rating]
            })
            self.book_list = pd.concat([self.book_list,new_book], ignore_index=True)
            self.num_books = len(self.book_list['book_name'])
        else:
            print(f"{book_name} already in book list")
        
    def has_read(self, book_name):
        if type(book_name) != str:
            raise TypeError(f"book name must be a string")
        if book_name in list(self.book_list['book_name']):
            return True
        else:
            return False
    
    def num_books_read(self):
        return len(self.book_list['book_name'])
    
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]