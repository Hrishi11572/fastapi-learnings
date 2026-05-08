from fastapi import FastAPI, Body  # type: ignore
from pydantic import BaseModel # type: ignore

app = FastAPI()


# Lets create a Book python object
class Book: 
    
    id: int 
    title : str 
    author : str 
    description: str 
    rating : int 
    
    def __init__ (self, id, title, author, description, rating): 
        self.id = id 
        self.title = title 
        self.author = author 
        self.description = description
        self.rating = rating
    

# VALIDATE YOUR BOOK REQUEST and then convert the data to Book()

class BookRequest(BaseModel): 
    id: int 
    title: str 
    author : str 
    description : str 
    rating : int 

     
BOOKS = [
    Book(1, "Introduction to Graphs", "Hrishikesh", "CS Book" , 4.5), 
    Book(2, "Faster FastAPI", "margot robbie", "great book", 5), 
    Book(3, "Midjourney Crisis", "dakota jhonson", "brilliant novel", 4), 
    Book(4, "Jane Austere Milley", "Ana D Armas", "gothic Novel", 5), 
]

@app.get("/")
async def helloWorld(): 
    return "Hello World!"

# GET METHOD

@app.get("/books")
async def getAllBooks(): 
    return BOOKS


# POST METHOD 

@app.post("/createBook")
async def createBook(book_request : BookRequest): 
    newBook = Book(**book_request.model_dump())
    print(type(newBook))
    BOOKS.append(newBook)
    
    
