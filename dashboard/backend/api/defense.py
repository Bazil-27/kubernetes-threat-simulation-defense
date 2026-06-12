from fastapi import APIRouter
from models.defense import DefenseEvent, DefenseSummary, KubescapeScore

router = APIRouter()

EVENTS = [
    DefenseEvent(
        id=1,
        tool="Tetragon",
        event="cat /etc/shadow executed inside privileged pod",
        namespace="vuln-apps",
        blocked=False,
        severity="critical"
    ),
    DefenseEvent(
        id=2,
        tool="OPA Gatekeeper",
        event="Privileged container deployment blocked",
        namespace="vuln-apps",
        blocked=True,
        severity="critical"
    ),
    DefenseEvent(
        id=3,
        tool="OPA Gatekeeper",
        event="Unknown registry image blocked",
        namespace="vuln-apps",
        blocked=True,
        severity="high"
    ),
    DefenseEvent(
        id=4,
        tool="Network Policy",
        event="Unauthorized pod-to-pod traffic dropped",
        namespace="monitoring",
        blocked=True,
        severity="medium"
    ),
    DefenseEvent(
        id=5,
        tool="Tetragon",
        event="kubectl exec into running container detected",
        namespace="vuln-apps",
        blocked=False,
        severity="high"
    ),
]

SCORE = KubescapeScore(
    overall=75.0,
    mitre=67.89,
    nsa=65.90
)

@router.get("/", response_model=DefenseSummary)
def get_defense():
    return DefenseSummary(score=SCORE, events=EVENTS)

@router.get("/score", response_model=KubescapeScore)
def get_score():
    return SCORE

@router.get("/events")
def get_events():
    return EVENTS
