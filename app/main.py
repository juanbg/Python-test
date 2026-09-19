from fastapi import FastAPI, HTTPException, Response, status

from app.models import User, UserCreate, UserUpdate
from app.repository import (
    create_user,
    delete_user,
    get_all_users,
    get_user_by_id,
    update_user,
)

app = FastAPI(
    title="Simple In-Memory CRUD API",
    description="CRUD de ejemplo sin base de datos. Los datos viven en memoria.",
    version="1.0.0",
)


@app.get("/")
def health_check():
    return {"status": "ok", "message": "API funcionando"}


# 1. CREATE
@app.post("/users", response_model=User, status_code=status.HTTP_201_CREATED)
def create(data: UserCreate):
    return create_user(data)


# 2. READ ALL
@app.get("/users", response_model=list[User])
def read_all():
    return get_all_users()


# 3. READ ONE
@app.get("/users/{user_id}", response_model=User)
def read_one(user_id: int):
    user = get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# 4. UPDATE
@app.put("/users/{user_id}", response_model=User)
def update(user_id: int, data: UserUpdate):
    user = update_user(user_id, data)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# 5. DELETE
@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(user_id: int):
    deleted = delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
