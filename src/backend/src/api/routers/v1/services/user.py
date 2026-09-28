from aiogram.utils.web_app import WebAppInitData
from src.api.core.base_service import BaseService, ServiceResponse

from src.db.models.user import User
from src.db.schemas import UserSchema

class UserService(BaseService):
    async def get_me(self, auth_data: WebAppInitData) -> ServiceResponse:
        user = await User.filter(user_id=auth_data.user.id).exists()
        if not user:
            user = await User.create(
                user_id=auth_data.user.id,
                name=auth_data.user.first_name,
                username=auth_data.user.username
            )
        user_obj = (
            await UserSchema.from_tortoise_orm(user)
        ).model_dump(mode="json", by_alias=True)
        
        return self.success(user_obj)