from fastapi import APIRouter
from langchain import LangChain

router = APIRouter()

@router.post('/process')
async def process_data(data: dict):
    # Simulate AI processing
    chain = LangChain()
    result = chain.process(data)
    return {"processed": result}
