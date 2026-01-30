from fastapi import APIRouter

router = APIRouter()

@router.get('/make-decision')
async def make_decision(criteria: str):
    # Simulate decision making
    if criteria == "criterion1":
        decision = "Decision A"
    else:
        decision = "Decision B"
    return {"decision": decision}
