from fastapi import APIRouter
from app.routers import crud_route

router = APIRouter()
router.include_router(crud_route.router, tags=["Users"])