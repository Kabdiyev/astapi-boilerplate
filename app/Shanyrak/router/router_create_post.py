from app.utils import AppModel
from fastapi import Depends, Response

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data

from ..service import Service, get_service
from . import router


class CreatePostResponse(AppModel):
    type: str
    address: str
    rooms: float
    phone: int


class CreatePostRequest(AppModel):
    type: str
    address: str
    rooms: float
    phone: int


@router.post("/", response_model=CreatePostResponse)
def create_post(
    input: CreatePostRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    user_id = jwt_data.user_id
    post = input.dict()
    svc.repository.create_post(user_id, post)

    return Response(status_code=200)
