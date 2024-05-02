from work.contrib.schemas import BaseSchema
from typing import Annotated
from pydantic import Field

class Categoria(BaseSchema):
    nome: Annotated[str, Field(description='Nome da categoria', example='Scale', max_length=10)]