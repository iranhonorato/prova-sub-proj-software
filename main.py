from fastapi import FastAPI, HTTPException, Header
from typing import List, Optional
from uuid import UUID

from model import Avaliacao, AvaliacaoDTORequest, AvaliacaoDTOResponse
from database import collection_avaliacoes

app = FastAPI()


@app.post("/avaliacoes", response_model=AvaliacaoDTOResponse, status_code=201)
async def cadastrar_avaliacao(body: AvaliacaoDTORequest, role: Optional[str] = Header(default=None)):
    if role != "ADMIN":
        raise HTTPException(status_code=403, detail="Apenas ADMIN pode cadastrar avaliações")

    avaliacao = Avaliacao(**body.model_dump())
    doc = avaliacao.model_dump()
    doc["id"] = str(doc["id"])

    await collection_avaliacoes.insert_one(doc)
    return avaliacao


@app.get("/avaliacoes", response_model=List[AvaliacaoDTOResponse])
async def listar_avaliacoes(role: Optional[str] = Header(default=None)):
    if role not in ("ADMIN", "USER"):
        raise HTTPException(status_code=403, detail="Role inválida ou ausente")

    docs = await collection_avaliacoes.find({}, {"_id": 0}).to_list(length=None)
    return docs


@app.delete("/avaliacoes/{id}", status_code=204)
async def deletar_avaliacao(id: UUID, role: Optional[str] = Header(default=None)):
    if role != "ADMIN":
        raise HTTPException(status_code=403, detail="Apenas ADMIN pode deletar avaliações")

    result = await collection_avaliacoes.delete_one({"id": str(id)})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
