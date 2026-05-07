# GET Method: 

from fastapi import FastAPI  # pyright: ignore[reportMissingImports]

app = FastAPI()

BOOKS = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "category": "Novel", "published_year": 1925, "rating": 4.5, "price": 10.99},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "category": "Novel", "published_year": 1960, "rating": 4.8, "price": 12.99},
    {"title": "1984", "author": "George Orwell", "category": "Dystopian", "published_year": 1949, "rating": 4.7, "price": 9.99},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "category": "Romance", "published_year": 1813, "rating": 4.6, "price": 7.99},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "category": "Novel", "published_year": 1951, "rating": 4.3, "price": 11.99}
]

@app.get("/")
async def baseURL():
    return {"message" : "welcome to basics of dev"}

@app.get("/books")
async def readAllBooks():
    return f"Here are all the books \n {BOOKS}"


@app.get("/books/{book_title}")
async def readBooks(book_title : str): 
    for book in BOOKS: 
        if book.get("title").casefold() == book_title.casefold(): 
            return book 
    
    return "BOOK NOT FOUND."

# Filtering books by category using query parameters 

@app.get("/books/")
async def getBooksByCategory(category : str):
    books_by_cat = []
    for book in BOOKS: 
        if book.get("category").casefold == category.casefold():
            books_by_cat.append(book)
    
    return books_by_cat

# Filtering books of a particular author by category using both path params and query params 

@app.get("/books/{author_}/")
async def getBooksOfAuthByCat(author_: str , category : str): 
    db = []
    for book in BOOKS: 
        if book.get("author").casefold() == author_.casefold(): 
            if book.get("category").casefold() == category.casefold(): 
                db.append(book)
    
    return db