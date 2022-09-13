import requests
from datetime import datetime
import aiohttp
import asyncio


async def main():

    async with aiohttp.ClientSession() as session:

        url = "http://127.0.0.1:8000/askdoc/chat-api/v1"
        async with session.post("http://127.0.0.1:8000/askdoc/chat-api/v1", json={"message": "I want to report a crime"}) as resp:
            res = await resp.json()
            print(res)

loop = asyncio.get_event_loop()

tasks = []
# I'm using test server localhost, but you can use any url

start = datetime.now()
for i in range(500):
    task = asyncio.ensure_future(main())
    tasks.append(task)
loop.run_until_complete(asyncio.wait(tasks))
print(datetime.now() - start)