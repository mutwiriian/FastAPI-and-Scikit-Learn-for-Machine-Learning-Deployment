from fastapi import APIRouter, Request, Depends, HTTPException,status
from models.prediction import TemperaturePrediction
from models.payload import TemperaturePredictionPayload
from enum import Enum

router = APIRouter()

#set model types available to user
class ModelType(str,Enum):
    RF='random_forest'
    SVR='support_vector'
    LGBM='lightgbm'

#run predction at endpoint from the FastAPI app object
@router.post("/model_deploy/{model_type}",
             response_model= TemperaturePrediction)
async def predict(request: Request,model_type: ModelType,
                  payload: TemperaturePredictionPayload) -> TemperaturePrediction:     
       
    if model_type==ModelType.RF:
        model = request.app.state.model_rf
    elif model_type==ModelType.SVR:
        model = request.app.state.model_svr
    else:
        model = request.app.state.model_lgbm
    prediction: TemperaturePrediction = model.predict(payload)
    return prediction