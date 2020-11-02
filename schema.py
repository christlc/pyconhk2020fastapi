from typing import Optional
from pydantic import BaseModel


class Message(BaseModel):
    message: str
    meta: Optional[dict] = None
