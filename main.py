#import library
from fastapi import FastAPI, HTTPException, Header
import pandas as pd
import uvicorn

#create instance/object
app = FastAPI()

#define API KEY
apiKey = "bikeshare_api"

#define endpoint home
@app.get("/")
def home():
    return {"message": "Welcome to San Fransisco Bike Share!"}

#define url -> endpoint
@app.get("/show")
def show_data(key: str = Header(None)):
    df = pd.read_csv("no_outlier.csv")
    return df.to_dict(orient='records')

#define url -> delete endpoint
@app.delete("/delete/duration/{duration}")
def delete_data(duration:int):
    df = pd.read_csv("no_outlier.csv")
    if duration not in df["duration_sec"].values:
        raise HTTPException(status_code = 404, detail = 'data tidak ditemukan')
    else:
        df.drop(df[df["duration_sec"]== duration].index, inplace=True)
        return "data berhasil dihapus"

if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)


