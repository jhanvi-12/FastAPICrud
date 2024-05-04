from constant import constant
from fastapi.responses import JSONResponse

class StandardResponse:
    def __init__(self, status: int, data: dict, message: str) -> None:
        """This function defines arguments that are used in the class

        Arguments:
            status (int): The http status response from API
            data (dict/list): The Data from API
            message (str): The message from the API

        Returns:
            Returns the API standard response
        """
        self.status = status
        self.data = data
        self.status_code = status
        self.message = message

    @property
    def make(self):
        """This method is called to create a new instance of the standard response."""
        self.status = (
            constant.STATUS_SUCCESS 
            if self.status in [200, 201]
            else constant.STATUS_ERROR
        )
        response = {'status': self.status, "data": self.data, "message": self.message}
        return JSONResponse(content=response, status_code=self.status_code)