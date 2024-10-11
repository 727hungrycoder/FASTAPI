from fastapi import Body,FastAPI

app = FastAPI()

BOOKS =[
    {'title': 'Title One', 'author': 'Author One', 'description': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'description': 'science'},   
    {'title': 'Title Three', 'author': 'Author Three', 'description': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'description': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'description': 'math'},
    {'title': 'Title Six', 'author': 'Author Six', 'description': 'math'}
]
@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def read_book(book_title:str,new_book = Body()):
    for book in BOOKS:
        if book['title'].casefold() == book_title.casefold():
            return book
        



@app.get("/books/")
async def read_category_by_query(description:str):
    books_to_return = []
    for book in BOOKS:
        if book['description'].casefold() == description.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/books/{book_author}")
async def read_author_category_query(book_author:str, description:str):
    books_to_return = []
    for book in BOOKS:
        if book['author'].casefold() == book_author.casefold() and book['description'].casefold() == description.casefold():
            books_to_return.append(book)
    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book = Body()):
    BOOKS.append(new_book)
    
    
@app.put("/books/update_book")
async def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold()== updated_book.get('title').casefold():
            BOOKS[i]=updated_book
            
            


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title:str):
    for i in range(len(BOOKS)): 
        if BOOKS[i].get('title').casefold()== book_title.casefold():
            BOOKS.pop(i)
            break
        


"""Get all books from specific author using path or query parameters"""

@app.get("/books/byauthor/{book_author}")
async def read_author_category(book_author:str):
    books_to_return = []
    for book in BOOKS:
        if book['author'].casefold() == book_author.casefold():
            books_to_return.append(book)
    return books_to_return

