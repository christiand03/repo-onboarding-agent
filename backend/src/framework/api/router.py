from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def main_route() -> str:
    return {"message":"Hello World"}

@router.get("/agent/{agent_id}")
def repo_agent_router(agent_id: str):
    return {"Agent": agent_id}