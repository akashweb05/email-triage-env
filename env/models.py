from pydantic import BaseModel
from typing import List

class Observation(BaseModel):
    email_text: str
    sender: str
    history: List[str]

class Action(BaseModel):
    label: str
    priority: int
    reply: str