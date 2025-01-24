from pydantic import BaseModel

class FBParserResponce(BaseModel):
    cookie: str
    token: str