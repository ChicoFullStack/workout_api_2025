from fastapi import APIRouter
from workout_api.atleta.controller import router as atleta
from workout_api.categorias.controller import router as categorias
from workout_api.centro_treinamento.controller import router as centros_trinamento


api_router = APIRouter()
api_router.include_router(atleta, prefix='/atletas', tags=['atletas'])
api_router.include_router(categorias, prefix='/categorias', tags=['categorias'])
api_router.include_router(centros_trinamento, prefix='/centros_treinamentos', tags=['centros_treinamentos'])

