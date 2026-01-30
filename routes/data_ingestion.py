from fastapi import APIRouter

router = APIRouter()

@router.post('/ingest')
async def ingest_data(data: dict):
    # Simulate data ingestion
    return {"status": "Data ingested", "data": data}
