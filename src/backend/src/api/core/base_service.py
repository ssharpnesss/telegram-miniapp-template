from typing import Any
from pydantic import BaseModel

class ServiceResponse(BaseModel):
    """"""
    ok: bool
    status: int = 200
    data: Any = None
    message: str | None = None

    @classmethod
    def success(
        cls,
        data: Any = None,
        message: str | None = None,
        status: int = 200
    ) -> "ServiceResponse":
        return cls(ok=True, status=status, data=data, message=message)

    @classmethod
    def error(
        cls,
        data: Any = None,
        message: str | None = None,
        status: int = 400
    ) -> "ServiceResponse":
        return cls(ok=False, status=status, data=data, message=message)

    def response(self) -> dict[str, Any]:
        return {
            "content": {
                "data": self.data,
                "message": self.message,
                "ok": self.ok
            },
            "status_code": self.status
        }

class BaseService:
    def success(
        self,
        data: Any = None,
        message: str | None = None,
        status: int = 200
    ) -> ServiceResponse:
        return ServiceResponse.success(data=data, message=message, status=status)

    def error(
        self,
        data: Any = None,
        message: str | None = None,
        status: int = 400
    ) -> ServiceResponse:
        return ServiceResponse.error(data=data, message=message, status=status)