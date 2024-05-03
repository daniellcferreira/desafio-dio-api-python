from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from work.centro_treinamento.models import CentroTreinamentoModel
from work.centro_treinamento.schemas import CentroTreinamentoIn, CentroTreinamentoOut
from work.contrib.dependencies import DatabaseDependecy
from sqlalchemy.future import select

router = APIRouter()

@router.post('/', summary='Criar um novo centro de treinamento', 
             status_code=status.HTTP_201_CREATED,
             response_model=CentroTreinamentoOut,
             )

async def post(
    db_session: DatabaseDependecy, 
    centro_treinamento_in: CentroTreinamentoIn= Body(...)
    ) -> CentroTreinamentoOut:

    centro_trinamento_out = CentroTreinamentoOut(id=uuid4(), **centro_treinamento_in.model_dump())
    centro_treinamento_model = CentroTreinamentoModel(**centro_trinamento_out.model_dump())

    db_session.add(centro_treinamento_model)
    await db.session.commit()

    return centro_trinamento_out

@router.get('/', summary='Consultar todos os centros de treinamento', 
             status_code=status.HTTP_200_OK,
             response_model=list[CentroTreinamentoOut]
             )

async def query(db_session: DatabaseDependecy) -> list[CentroTreinamentoOut]:
    centros_trinamento_out: list[CentroTreinamentoOut] = (await db_session.execute(select(CentroTreinamentoModel))).scalars().all()
    
    return centros_trinamento_out

@router.get('/{id}', summary='Consultar um centro de treinamento pelo ID', 
             status_code=status.HTTP_200_OK,
             response_model=CentroTreinamentoOut
             )

async def query(id: UUID4 ,db_session: DatabaseDependecy) -> CentroTreinamentoOut:
    centro_treinamento_out: CentroTreinamentoOut = (await db_session.execute(select(CentroTreinamentoModel).filter_by(id=id))).scalars().first()

    if not centro_treinamento_out:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Centro de treinamento não encontrada no id: {id}')
    
    return centro_treinamento_out