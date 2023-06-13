from typing import Any

from pydantic import Field
from fastapi import Depends

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel

from ..service import Service, get_service
from . import router


class GetMyPostResponse(AppModel):
    id: Any = Field(alias="_id")
    type: str
    address: str
    rooms: float
    phone: int


@router.get("/", response_model=GetMyPostResponse)
def get_post(
    idn: int,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    user_id = jwt_data.user_id
    results = svc.repository.get_post(user_id)

    return GetMyPostResponse(**results[idn])
