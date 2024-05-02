from fastapi import APIRouter, Body, status
from work.atleta.schemas import AtletaIn
from work.contrib.dependencies import DatabaseDependecy

router = APIRouter()

@router.post('/', summary='Criar novo atleta', status_code=status.HTTP_201_CREATED)
async def post(db_session: DatabaseDependecy, atleta_in: AtletaIn= Body(...)):
    pass