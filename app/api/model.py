from pydantic import BaseModel, Extra

class Book(BaseModel):
    """This class represents a book table model that 
    can be used to create book using mongoDB."""
    title: str
    author: str

    class Config:
        extra = Extra.forbid
        orm_mode = True
        extra = Extra.allow
        schema_extra = {
            "id": 1,
            "title": "The girl in the train",
            "author": "Tagore"
        }