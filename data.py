from fastapi import FastAPI
import pandas as pd


app = FastAPI()

baby_data = pd.read_csv('bnames.csv')


@app.get("/year/{year}")
def read_root(year: int):
    return baby_data[baby_data['year']==year].head(10).to_dict(orient='records')


@app.get("/yeartopnames/{year}")
def read_root(year: int):
    return baby_data[baby_data['year']==year].nlargest(10, 'percent').to_dict(orient='records')


@app.get("/name/{name}")
def read_name(name: str):
    return {
        'mean': baby_data[baby_data['name']==name]['percent'].mean(),
        'data': baby_data[baby_data['name']==name].to_dict(orient='records')
    }




if __name__ == "__main__":
    import uvicorn
    uvicorn.run("data:app", host="0.0.0.0", port=8000, log_level="info", workers=1, reload=True)
