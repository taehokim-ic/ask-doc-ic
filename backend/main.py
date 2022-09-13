from pydantic import BaseModel
from nlu.nlu_engine import nlu_engine
from repo import *
from sqlalchemy.ext.asyncio import AsyncSession     
from fastapi import FastAPI, Depends
from db.db import get_session, init_db 
from models.data_models import *


from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import Response

app = FastAPI()

async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception:
        # you probably want some kind of logging here
        return Response("Internal server error", status_code=500)
        
app.middleware('http')(catch_exceptions_middleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str
    
    class Config:
        orm_mode = True

@app.on_event("startup")
async def on_startup():
    await init_db()
    
@app.get('/askdoc/chat-api/v1')
async def chatbot():
    return {'message': 'hello!, perhaps you want to make a post request'}
    

@app.post('/askdoc/chat-api/v1') # Might want to change end point to "/askdoc/chat-api/v1/chat'
async def process_message(client_message: Message = None, session: AsyncSession = Depends(get_session)):
    
    message = client_message.message
    await add_message(message=message, session=session)
    
    result = nlu_engine.parse(message)
    
    data = await get_intent_data(intent_result=result, session=session)
    
    if not data:
        return {
            "keyword_link_pair": data
        }
    
    return {
        "keyword_link_pair": [{"keyword": row[0].keyword, "link": row[0].link} for row in data]
    }