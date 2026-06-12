from pydantic import BaseModel
from typing import List
from models.attack import Attack
from models.defense import DefenseSummary

class Report(BaseModel):
    title: str
    phase: int
    attacks: List[Attack]
    defense: DefenseSummary
