from fastapi import Depends, Response

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel

from ..service import Service, get_service

from . import router


class UpdatePostRequest(AppModel):
    type: str
    address: str
    rooms: float
    phone: int


@router.patch("/")
def update_post(
    _id: str,
    input: UpdatePostRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    update_result = svc.repository.update_post(_id, jwt_data.user_id, input.dict())
    if update_result.modified_count == 1:
        return Response(status_code=200)
    return Response(status_code=404)
