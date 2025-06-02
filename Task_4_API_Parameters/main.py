from fastapi import FastAPI, Path, Query, Body, Header, Form, Cookie, File, UploadFile
from pydantic import BaseModel

app = FastAPI()

# Body Model
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float 

# ✅ 1. Path Parameter
@app.get("/items/{item_id}")
async def read_item(
    item_id: int = Path(..., title="Item Id", ge= 1)
):
    return {"item_id": item_id}

# ✅ 2. Query Parameters
@app.get("/items/")
async def read_items(
    q: str | None = Query(None, min_length = 3, max_length = 50),
    skip: int = Query(0, ge = 0),
    limit: int = Query(10, le = 100)
):
    return {"q": q, "skip": skip, "limit": limit }
 
# ✅ 3. Body Parameters
@app.post("/items/") 
async def create_item(
    item: Item = Body(..., description = "Item data JSON Body")
):
    return {"item": item.model_dump()}

# ✅ 4. Header Parameters
@app.get("/header-info/")
async def get_header_info(
    user_agent: str | None = Header(None)
):
    return {"user_agent": user_agent}

# ✅ 5. Form Parameters
@app.post("/login/")
async def login(
    username : str = Form(...),
    password: str = Form(...)
):
    return {"username": username, "message": "Login Successful"}

# ✅ 6. Cookie Parameters
@app.get("/cookie/")
async def read_cookie(
    session_id : str | None = Cookie(None)
):
    return {"session_id": session_id}
    
# ✅ 7. File Upload Parameters
@app.post("/upload/")
async def upload_file(
    file: UploadFile = File(...)
):
    return {
        "upload_file": file.filename,
        "content_type": file.content_type
    }