from pydantic import BaseModel
from typing import List

class DefenseEvent(BaseModel):
    id: int
    tool: str                  # e.g. "Tetragon", "OPA Gatekeeper"
    event: str                 # e.g. "cat /etc/shadow detected"
    namespace: str             # e.g. "vuln-apps"
    blocked: bool              # True = blocked, False = detected only
    severity: str              # e.g. "high"

class KubescapeScore(BaseModel):
    overall: float             # 75.0
    mitre: float               # 67.89
    nsa: float                 # 65.90

class DefenseSummary(BaseModel):
    score: KubescapeScore
    events: List[DefenseEvent]
