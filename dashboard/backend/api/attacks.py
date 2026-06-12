from fastapi import APIRouter
from models.attack import Attack, AttackList

router = APIRouter()

ATTACKS = [
    Attack(
        id=1,
        name="SQL Injection",
        technique="UNION-based credential dump",
        mitre_id="T1190",
        mitre_tactic="Initial Access",
        target="DVWA",
        result="success",
        severity="critical"
    ),
    Attack(
        id=2,
        name="Command Injection",
        technique="OS command execution via web form",
        mitre_id="T1059",
        mitre_tactic="Execution",
        target="DVWA",
        result="success",
        severity="critical"
    ),
    Attack(
        id=3,
        name="Container Escape",
        technique="Privileged pod host filesystem mount",
        mitre_id="T1611",
        mitre_tactic="Privilege Escalation",
        target="Privileged Pod",
        result="success",
        severity="critical"
    ),
    Attack(
        id=4,
        name="RBAC Escalation",
        technique="Service account token cluster enumeration",
        mitre_id="T1078",
        mitre_tactic="Defense Evasion",
        target="Kubernetes API",
        result="success",
        severity="high"
    ),
    Attack(
        id=5,
        name="Secrets Extraction",
        technique="Plaintext ENV var credential dump",
        mitre_id="T1552",
        mitre_tactic="Credential Access",
        target="Running Container",
        result="success",
        severity="high"
    ),
]

@router.get("/", response_model=AttackList)
def get_attacks():
    return AttackList(total=len(ATTACKS), attacks=ATTACKS)

@router.get("/{attack_id}", response_model=Attack)
def get_attack(attack_id: int):
    for a in ATTACKS:
        if a.id == attack_id:
            return a
