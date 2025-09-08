def individual_todo(todo):
    return{
        "id":str(todo["_id"]),
        "title":todo["title"],
        "description":todo["description"],
        "isCompleted":todo["isCompleted"]
    }
def all_todo(todos):
    return [individual_todo(todo) for todo in todos]