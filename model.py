from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID, uuid4




class Avaliacao(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    email_avaliador: str
    email_avaliado: str
    comentarios: str
    nota: float = Field(ge=0, le=10)
    data_avaliacao: datetime


class AvaliacaoDTORequest(BaseModel):
    email_avaliador: str
    email_avaliado: str
    comentarios: str
    nota: float = Field(ge=0, le=10)
    data_avaliacao: datetime


class AvaliacaoDTOResponse(BaseModel):
    id: UUID
    email_avaliador: str
    email_avaliado: str
    comentarios: str
    nota: float
    data_avaliacao: datetime
