from fastapi import FastAPI
from loguru import logger
from routes import ai_processing, data_ingestion, decision_making

app = FastAPI(title="Modular Monolith with AI-Augmented Architecture")

# Include routers for different modules
app.include_router(ai_processing.router, prefix='/ai')
app.include_router(data_ingestion.router, prefix='/data')
app.include_router(decision_making.router, prefix='/decision')

@app.get('/')
async def root():
    return {"message": "Welcome to the Modular Monolith Application"}
