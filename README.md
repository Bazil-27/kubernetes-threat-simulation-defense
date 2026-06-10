# Kubernetes Threat Simulation & Defense
> "Attack Like a Hacker. Defend Like an Engineer."

A hands-on Kubernetes security lab built from scratch to simulate real-world attacks and practice detection and defense.

## Lab Architecture
- 3-node Kubernetes cluster (Kind)
- Vulnerable targets: DVWA, OWASP Juice Shop
- Intentional misconfigs: privileged pods, wildcard RBAC, plaintext secrets
- Monitoring: Prometheus + Grafana + Node Exporter
- Runtime detection: Tetragon (eBPF)

## Attack Coverage (Phase 2)
| Attack | Technique | Status |
|---|---|---|
| SQL Injection | UNION-based, credential dump | ✅ |
| Command Injection | OS command execution, /etc/passwd | ✅ |
| Container Escape | Privileged pod, host mount | ✅ |
| RBAC Escalation | Service account token abuse | ✅ |
| Secrets Extraction | Plaintext ENV credentials | ✅ |

## Phases
- [x] Phase 1 — Infra & Lab Setup
- [x] Phase 2 — Attack Simulation
- [ ] Phase 3 — Detection & Defense
- [ ] Phase 4 — Hardening & Automation