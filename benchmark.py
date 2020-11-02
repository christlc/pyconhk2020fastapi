from fastapi import FastAPI
import time
import asyncio

app = FastAPI()


@app.get("/benchmark1/")
async def benchmark():
    await asyncio.sleep(1)
    return {"message": "ok"}


@app.get("/benchmark2/")
def benchmark2():
    time.sleep(1)
    return {"message": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", workers=1)


# benchmark
# ab -n 100 -c 10 http://127.0.0.1:8000/benchmark1/
# ab -n 100 -c 10 http://127.0.0.1:8000/benchmark2/
# ab -n 100 -c 50 http://127.0.0.1:5000/benchmark2/


