from fastapi import APIRouter

router = APIRouter(prefix="/posts", tags=["posts"])


# Получение поста по id
@router.get("/{post_id}")
def get_post(post_id: int):
    return {"post_id": post_id}


# Создание поста
@router.post("/")
def create_post(body: dict):
    return {"body": body}


# Обновление поста
@router.put("/{post_id}")
def update_post(post_id: int):
    return {"post_id": post_id}


# Удаление поста
@router.delete("/{post_id}")
def delete_post(post_id: int):
    return {"post_id": post_id}
