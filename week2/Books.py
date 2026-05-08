from fastapi import FastAPI, Body, Path  # type: ignore
from pydantic import BaseModel, Field # type: ignore
from typing import Optional

app = FastAPI()


# Lets create a Book python object
class Book: 
    
    id: int 
    title : str 
    author : str 
    description: str 
    rating : float
    published_date : int
    
    def __init__ (self, id, title, author, description, rating, published_date): 
        self.id = id 
        self.title = title 
        self.author = author 
        self.description = description
        self.rating = rating
        self.published_date = published_date
    

# VALIDATE YOUR BOOK REQUEST and then convert the data to Book()

class BookRequest(BaseModel): 
    id : Optional[int] = Field(description = "Id is not needed at instantiation", default=None)
    title: str = Field(min_length = 3)
    author : str = Field(min_length = 3)
    description : str = Field(min_length = 1, max_length = 180)
    rating : float = Field(gt=-1, lt=6)
    published_date : int = Field(gt=0)
    
    model_config = {
        "json_schema_extra": {
            "example" : {
                "title" : "a new book", 
                "author" : "Hrishikesh Tiwari", 
                "description" : "a new description of book", 
                "rating" : 5, 
                "published_date" : 2010
            }
        }
    }

     
BOOKS = [
    Book(1, "Introduction to Graphs", "Hrishikesh", "CS Book" , 4.5, 2020), 
    Book(2, "Faster FastAPI", "margot robbie", "great book", 5, 2019), 
    Book(3, "Midjourney Crisis", "dakota jhonson", "brilliant novel", 4, 2011), 
    Book(4, "Jane Austere Milley", "Ana D Armas", "gothic Novel", 5, 2004), 
]

@app.get("/")
async def helloWorld(): 
    return "Hello World!"

# GET METHOD

@app.get("/books")
async def getAllBooks(): 
    return BOOKS


@app.get("/books/{book_id}")
async def getABook(book_id: int = Path(gt=0)): # path param must be gt 0
    for book in BOOKS: 
        if book.id == book_id: 
            return book 
    
    return "Book Not Found!"


@app.get("/books/by-rating/")
async def readBookByRating(book_rating : int): 
    book_to_return = []
    for book in BOOKS: 
        if book.rating == book_rating: 
            book_to_return.append(book)
            
    return book_to_return


@app.get("/books/by-date/")
async def readBooksByDate(publishDate: int): 
    books_to_return = []
    for book in BOOKS: 
        if book.published_date == publishDate: 
            books_to_return.append(book)

    return books_to_return


# POST METHOD 

@app.post("/createBook")
async def createBook(book_request : BookRequest): # we removed Body() and used pydantic instead, to be able to do request validation 
    newBook = Book(**book_request.model_dump())
    print(type(newBook))
    # find the id, and then append the book to BOOKS
    BOOKS.append(find_book_id(newBook))
    
    
def find_book_id(book : Book):
    if len(BOOKS) > 0: 
        book.id = BOOKS[-1].id + 1
    else: 
        book.id = 1     
    return book


# PUT METHOD 

@app.put("/books/update_book")
async def update_book(book : BookRequest):
    for i in range(len(BOOKS)): 
        if BOOKS[i].id == book.id: 
            BOOKS[i] = book # update the book with the same id 


# DELETE METHOD 

@app.delete("/books/{book_id}")
async def deleteBook(book_id : int): 
    for i in range(len(BOOKS)): 
        if BOOKS[i].id == book_id: 
            BOOKS.pop(i)
            break 
