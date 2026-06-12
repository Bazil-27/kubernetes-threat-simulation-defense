from pydantic import BaseModel
from typing import List, Optional

class Attack(BaseModel):
    id: int
    name: str                  # e.g. "SQL Injection"
    technique: str             # e.g. "UNION-based credential dump"
    mitre_id: str              # e.g. "T1190"
    mitre_tactic: str          # e.g. "Initial Access"
    target: str                # e.g. "DVWA"
    result: str                # e.g. "success"
    severity: str              # e.g. "critical"

class AttackList(BaseModel):
    total: int
    attacks: List[Attack]
