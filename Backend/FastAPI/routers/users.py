from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Inicia url server: uvicorn users:app --reload

# Entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

# Lista de usuarios
users_list = [
    User(id=1, name="José", surname="Odé", url="https://jose.ode", age=32),
    User(id=2, name="Dayana", surname="Salvador", url="https://dayi.sal", age=27),
    User(id=3, name="Mario", surname="Lang", url="https://mario.lg", age=54)
]

@router.get("/usersjson")
async def usersjson():
    return [{"name": "José", "surname": "Odé", "url": "https://jose.ode", "age": 32},
            {"name": "Dayana", "surname": "Salvador", "url": "https://dayi.sal", "age": 27},
            {"name": "Mario", "surname": "Lang", "url": "https://mario.lg", "age": 54}]

@router.get("/users")
async def get_users():
    return users_list

# Path
@router.get("/user/{id}")
async def get_user_by_id(id: int):
    return search_user(id)

# Query
@router.get("/user/")
async def get_user_by_query(id: int):
    return search_user(id)

@router.post("/user/", response_model = User, status_code=201)
async def create_user(user: User):
    if isinstance(search_user(user.id), User):  # Cambiar la verificación a isinstance
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    
    else:
        users_list.append(user)
        return user  # Devuelve el nuevo usuario agregado
    
@router.put("/user/")
async def modifyuser(user: User):
    
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
            
    if not found:
        return {"Error": "No se ha actualizado el usuario"}
    
    return user

@router.delete("/user/{id}")
async def deleteuser(id: int):
    
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
            
    if not found:
        return {"Error": "No se ha eliminado el usuario"}

def search_user(id: int):
    users = list(filter(lambda user: user.id == id, users_list))
    if users:
        return users[0]
    else:
        return {"Error": "No se ha encontrado el usuario"}
