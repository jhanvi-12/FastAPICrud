from utils.database import collection, id_counter_collection
from fastapi import status
from app.api.model import Book
from fastapi.encoders import jsonable_encoder
from utils.standard_response import StandardResponse
from constant.constant import SuccessMessage, ErrorMessage

class BookService:
    def create_book_service(self, data: dict):
        """This function is used to create a book service.
        Args:
            data: dictionary
        Returns:
            response: dictionary
        """
        try:
            title_exist = collection.find_one({"title": data["title"]})
            # check if title exists in the collection or not.
            if title_exist:
                return StandardResponse(
                    status.HTTP_400_BAD_REQUEST,
                    None,
                    ErrorMessage.BOOK_ALREADY_EXISTS
                ).make

            res = Book(
                title=data.get('title'),
                author=data.get('author')
            )
            counter_doc = id_counter_collection.find_one_and_update({}, {"$inc": {"value": 1}},
                                                      upsert=True, return_document=True)
            new_id = counter_doc["value"]
            res.id = new_id
            collection.insert_one(res.dict())
            data = jsonable_encoder(res)
            return StandardResponse(status.HTTP_201_CREATED,
                                    data,
                                    SuccessMessage.BOOK_CREATED).make
        except Exception:
            return StandardResponse(status.HTTP_400_BAD_REQUEST,
                                    None,
                                    ErrorMessage.ERROR_OCCURED).make

    def list_book_service(self):
        """This function is used to list the book service"""
        try:
            data_dict = collection.find()
            response = []
            for i in data_dict:
                if "_id" in i:
                    i["_id"] = str(i["_id"])
                response.append(i)

            return StandardResponse(
                status.HTTP_200_OK,
                response,
                SuccessMessage.INFO_FETCHED
            ).make
        except Exception:
            return StandardResponse(
                status.HTTP_400_BAD_REQUEST,
                None,
                ErrorMessage.NO_BOOK_DATA_FOUND
            )
    
    def update_book_service(self, id: int, 
                            data: dict):
        """This method updates the book service for the given book id."""
        try:
            find_book = collection.find_one({"id": id})
            title_exist = collection.find_one({"title": data["title"]})
            # check if title exists in the collection or not.
            if title_exist:
                return StandardResponse(
                    status.HTTP_400_BAD_REQUEST,
                    None,
                    ErrorMessage.BOOK_ALREADY_EXISTS
                ).make
            if find_book is None:
                return StandardResponse(
                status.HTTP_400_BAD_REQUEST,
                None,
                ErrorMessage.NO_BOOK_DATA_FOUND
            )
            if data:
                # update the book data with the new data using mongodb.
                collection.update_one({"id": id}, {"$set": 
                                                   {"title": data["title"], "author": data["author"]}})
                if "_id" in find_book:
                    find_book["_id"] = str(find_book["_id"])
                return StandardResponse(status.HTTP_200_OK,
                                        find_book,
                                        SuccessMessage.UPDATED_SUCCESS).make
        except Exception:
            return StandardResponse(status.HTTP_400_BAD_REQUEST,
                                    None,
                                    ErrorMessage.UPDATE_ERROR).make
    
    def delete_book(self, id: int):
        """This method deletes a book from the database."""
        try:
            find_book = collection.find_one({"id": id})
            if find_book is None:
                return StandardResponse(
                status.HTTP_400_BAD_REQUEST,
                None,
                ErrorMessage.NO_BOOK_DATA_FOUND
            )
            result = collection.delete_one({"id": id})
            if result.acknowledged:
                return StandardResponse(status.HTTP_200_OK,
                                        None,
                                        SuccessMessage.DELETED_SUCCESS).make
        except Exception:
            return StandardResponse(status.HTTP_400_BAD_REQUEST,
                                    None,
                                    ErrorMessage.DELETE_ERROR).make

    def query_items_service(self, keyword, limit):
        """This method is used to find items for given keyword."""
        query = {}
        if keyword:
            query = {"title": {"$regex": f".*{keyword}.*"}}
        items = []
        for item in collection.find(query).limit(limit):
            if "_id" in item:
                item["_id"] = str(item["_id"])
            items.append({"id": str(item["_id"]), **item})

        return StandardResponse(
                status.HTTP_200_OK,
                items,
                SuccessMessage.INFO_FETCHED
            ).make