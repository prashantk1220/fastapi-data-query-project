from typing import List
from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from datastore import schemas, crud
from app import dependencies


router = APIRouter()


@router.get("/", response_model=List[schemas.PerformanceMetrics])
def read_metrics(skip: int = 0, limit: int = 5, db: Session = Depends(dependencies.get_db)):
    try:
        metrics = crud.get_performance_metrics(db, skip=skip, limit=limit)
        return metrics
    except Exception as e:
        return JSONResponse(status_code=400, content={"message": f"Failed to execute. Detail: {e}"})


@router.post("/query")
def query_metrics(query: schemas.QueryModel, db: Session = Depends(dependencies.get_db)):
    try:
        result = crud.dynamic_query_performance_metrics(db, query)
        return result
    except Exception as e:
        return JSONResponse(status_code=400, content={"message": f"Failed to execute. Detail: {e}"})
