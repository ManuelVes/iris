from fastapi import FastAPI, Depends
import pandas as pd
import uvicorn
from model import classes, Feature_type, model

app = FastAPI(title="API1", description="with FastAPI by Daniele Grotti", version="1.0")
# model = None
# @api1.on_event("startup")
# def load_model():
#     global model


@app.get("/", status_code=200)
def home():
    return {" ---->          http://localhost:8000/docs     <----------"}


@app.get("/predict", status_code=200)
async def predict_get(data: Feature_type= Depends()):              # depends() input nelle celle
    try:
        data = pd.DataFrame(data)
        data = data.T
        data.rename(columns=data.iloc[0], inplace = True)
        data= data.iloc[1:]
        predictions = list(map(lambda x: classes[x], model.predict(data).tolist()))
        print(predictions)
        return {'prediction': predictions}                      #per pbi prediction=dict, per html json.dumps({'prediction': predictions})
    except:
        return {"prediction": "there was an error"} 

@app.post("/predict", status_code=200)
async def predict_post(data: Feature_type= Depends()):              # depends() input nelle celle
    try:
        data = pd.DataFrame(data)
        data = data.T
        data.rename(columns=data.iloc[0], inplace = True)
        data= data.iloc[1:]
        predictions = list(map(lambda x: classes[x], model.predict(data).tolist()))
        #print(predictions)
        return {'prediction': predictions}                   #per pbi prediction=dict, per html json.dumps({'prediction': predictions})
    except:
        return {"prediction": "there was an error"}        

@app.put("/predict", status_code=200)
async def predict_put(data: Feature_type= Depends()):              # depends() input nelle celle
    try:
        data = pd.DataFrame(data)
        data = data.T
        data.rename(columns=data.iloc[0], inplace = True)
        data= data.iloc[1:]
        predictions = list(map(lambda x: classes[x], model.predict(data).tolist()))
        #print(predictions)
        return {'prediction': predictions}                    #per pbi prediction=dict, per html json.dumps({'prediction': predictions})
    except:
        return {"prediction": "there was an error"}   


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000,reload=True)