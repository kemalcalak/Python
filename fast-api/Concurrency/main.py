from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/burgers')
async def read_burgers():
    burgers = await get_burgers(2)
    return burgers

async def get_burgers(number: int):
    # burgerleri oluşturmak için asenkron birkaç iş
    return burgers

burgers = get_burgers(2)

