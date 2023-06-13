from typing import Any
from fastapi import Depends, Response


from fastapi import Depends
from pydantic import Field

from app.utils import AppModel

from ..adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from .dependencies import parse_jwt_user_data


class UpdateMyAccountResponse(AppModel):
    phone: str = ""
    name: str = ""
    city: str = ""


class UpdateMyAccountRequest(AppModel):
    phone: str = ""
    name: str = ""
    city: str = ""


@router.patch("/", response_model=UpdateMyAccountResponse)
def update_user(
    input: UpdateMyAccountRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    svc.repository.update_user(jwt_data.user_id, input.dict())
    return Response(status_code=200)
