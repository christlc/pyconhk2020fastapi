from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
import numpy as np
import json

app = FastAPI()


@app.get("/v1/")
async def readv1():
    output = [{"none": None, "nan": np.nan}]
    print(json.dumps(output)) # not compliant json!!!!
    return output


@app.get("/v2/", response_class=ORJSONResponse)
async def readv2():
    return [{"none": None, "nan": np.nan}]


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("json_example:app", host="0.0.0.0", port=8000, log_level="info", workers=1, reload=True)
