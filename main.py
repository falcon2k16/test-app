from typing import Optional

from fastapi import FastAPI
import random
import string
import datetime


app = FastAPI()
version = "1.0.0"


@app.get("/")
async def read_root():
    return {"Test-app": version}


@app.get("/{account_id}")
async def read_item(account_id: int):
    return {"accountID": account_id, "version": version}


@app.get("/{account_id}/data")
async def read_item(account_id: int, length: Optional[int] = 16):
    random_string = await get_random_string(length)
    return {"accountID": account_id, "timestamp": datetime.datetime.utcnow(), "data": random_string}


async def get_random_string(length):
    # With combination of lower and upper case
    result_str = "".join(random.choice(string.ascii_letters) for i in range(length))
    # print random string
    return result_str
