"""This module is responsible for CRUD operations on the database usign MongoDB."""
from fastapi import APIRouter, Query
from app.api.model import Book
from app.api.service import BookService

router = APIRouter()

# Definfing CRUD operations on the database usign MongoDB.
@router.post("/create")
async def create_book(data: Book):
    """This API endpoint is used to create a new book."""
    data = data.dict()
    response = BookService().create_book_service(data)
    return response


@router.get("/")
async def list_book():
    """This API returns a list of books."""
    response = BookService().list_book_service()
    return response

@router.put("/update/book")
async def update_book(id: int, data: Book):
    """This API endpoint is used to update a book."""
    data = data.dict()
    response = BookService().update_book_service(id, data)
    return response

@router.delete("/")
async def delete_book(id: int):
    """This API endpoint is used to delete a book."""
    response = BookService().delete_book(id)
    return response

@router.get("/items/search/")
async def query_items(keyword: str = Query(None), limit: int = Query(10)):
    """This API is used to query items for a given keyword."""
    response = BookService().query_items_service(keyword, limit)
    return response
