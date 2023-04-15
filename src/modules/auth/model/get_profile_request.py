from src.modules.auth.model.user_model import BaseModel


class GetProfileRequest(BaseModel):
    user_id: str
