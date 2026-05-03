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
async def first_api(): 
    return BOOKS