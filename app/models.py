from pydantic import BaseModel

# creating TODO Model
class Todo(BaseModel):
    title:str
    description:str
    isCompleted:bool=False