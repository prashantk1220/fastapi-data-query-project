from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from app.endpoints import metrics_query
from .dependencies import insert_data

app = FastAPI(title="Performance Stats API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(metrics_query.router, prefix="/performance-metrics", tags=["metrics"])


@app.get("/")
async def main():
    await insert_data()
    return RedirectResponse(url="/docs/")

