from fastapi import FastAPI,APIRouter,HTTPException,status
from app.config import collection
from app.models import Todo
from bson import ObjectId
from app.schema import all_todo, individual_todo
from fastapi.responses import JSONResponse

app = FastAPI()
router=APIRouter()

# Creating a TODO
@router.post("/create-todo")
async def create_todo(new_task:Todo):
    try:
        res=await collection.insert_one(dict(new_task))
        return {"status_code":200,"message":"Todo Added Successfully","id":str(res.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Some Error Occurred {e}")

# Health Check
@router.get('/')
def health_checkup():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status_code":status.HTTP_200_OK,
            "status":"OK",
            "message":"FastAPI server is healthy"
        }
    )

# read All TODO
@router.get("/get-todo")
async def get_all_todos():
    if await collection.count_documents({}) == 0:
        return{"message":"TodoList is Empty!!!!!!!!!!!!!"}
    todos=await collection.find().to_list(length=1000)    
    return all_todo(todos)

# read TODO By id
@router.get("/todo/{id}")
async def get_todo_by_id(id:str):
    try:
        exist_todo=await collection.find_one({'_id':ObjectId(id)})
        if not exist_todo:
            raise HTTPException(status_code=404,detail=f"Not Found todo with id {id}.")
        return individual_todo(exist_todo)
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Something Went Wrong => {e}")

# Update TODO by id
@router.put("/update-todo/{id}")
async def update_todo(id:str,update_todo:Todo):
    try:
        exist_todo=await collection.find_one({'_id':ObjectId(id)})
        if not exist_todo:
            raise HTTPException(status_code=404,detail=f"Not Found todo with id {id}.")
        
        update_data=update_todo.model_dump()
        update_data.pop('_id',None)

        result=await collection.update_one(
            {"_id":ObjectId(id)},
            {"$set":update_data}
        )
        if result.modified_count==0:
            raise HTTPException(status_code=400, detail="No changes were made.", )

        updated=await collection.find_one({'_id':ObjectId(id)})
        return individual_todo(updated)
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Something Went Wrong => {e}")

# Delete TODO by id
@router.delete("/del-todo/{id}")
async def del_todo(id:str):
    try:
        exist_todo=await collection.find_one({'_id':ObjectId(id)})
        if not exist_todo:
            raise HTTPException(status_code=404,detail=f"Not Found todo with id {id}.")
        await collection.delete_one({'_id':ObjectId(id)})
        return{"message":"Deleted successfully"}    
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Something Went Wrong => {e}")

 # Delete all TODO
@router.delete("/delete-all")
async def delete_all_todo():
    try:
        if await collection.count_documents({}) == 0:
            return{"message":"TodoList is Empty!!!!!!!!!!!!!"} 
        await collection.drop()
        return{"message":"Deleted All"}
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Failed to Delete All => {e}")

app.include_router(router)