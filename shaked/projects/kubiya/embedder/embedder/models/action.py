from pydantic import BaseModel
from typing import Dict

class Action(BaseModel):
    parameters: Dict[str, Dict]
    description: str

class ActionStore(BaseModel):
    name: str
    actions: Dict[str, Action]

