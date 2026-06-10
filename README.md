# Kubernetes Threat Simulation & Defense
> "Attack Like a Hacker. Defend Like an Engineer."

A hands-on Kubernetes security lab built from scratch to simulate real-world attacks and practice detection and defense techniques used in production environments.

## Lab Architecture
- 3-node Kubernetes cluster (Kind) on WSL2
- Vulnerable targets: DVWA, OWASP Juice Shop
- Intentional misconfigs: privileged pods, wildcard RBAC, plaintext secrets in ENV
- Monitoring: Prometheus + Grafana + Node Exporter
- Runtime detection: Tetragon (eBPF)
- Policy enforcement: OPA Gatekeeper
- Security scanning: Kubescape

## Project Structure

KubeRedOps/
├── infra/kind/                  # Cluster config
├── vulnerable-apps/
│   ├── dvwa/                    # Damn Vulnerable Web App
│   └── juice-shop/              # OWASP Juice Shop
├── misconfigs/
│   ├── privileged-pod.yaml      # Privileged container misconfig
│   ├── rbac-wildcard.yaml       # Wildcard RBAC misconfig
│   └── secret-in-env.yaml       # Plaintext secrets in ENV
├── monitoring/
│   ├── prometheus.yaml
│   ├── grafana.yaml
│   └── node-exporter.yaml
├── defense/
│   ├── tetragon.yaml            # eBPF runtime detection
│   ├── tetragon-policy.yaml     # Custom TracingPolicy
│   ├── gatekeeper-no-privileged.yaml     # Block privileged pods
│   ├── gatekeeper-allowed-registries.yaml # Block unknown registries
│   ├── network-policies.yaml    # Default deny + namespace isolation
│   ├── auto-remediate.ps1       # Auto-kill suspicious pods (Windows)
│   ├── auto-remediate.sh        # Auto-kill suspicious pods (Linux)
│   └── kubescape-report.json    # Security scan results
├── attack-engine/
│   └── payloads.md              # All attack payloads documented
└── screenshots/                 # Phase-wise screenshots

## Phases

- [x] Phase 1 — Infra & Lab Setup
- [x] Phase 2 — Attack Simulation
- [x] Phase 3 — Detection & Defense
- [ ] Phase 4 — Hardening & Automation

## Phase 1 — Infra & Lab Setup

Built a full 3-node Kubernetes cluster locally using Kind on WSL2.

Deployed vulnerable targets and intentional misconfigurations to simulate a realistic attack surface.

**Stack:**
- Kind 3-node cluster
- DVWA (localhost:30000)
- OWASP Juice Shop (localhost:31000)
- Prometheus + Grafana (localhost:30001, 30002)
- Tetragon eBPF runtime detection

## Phase 2 — Attack Simulation

Simulated 5 real-world Kubernetes attacks against the lab.

| Attack | Technique | Result |
|--------|-----------|--------|
| SQL Injection | UNION-based credential dump | ✅ |
| Command Injection | OS command execution via web form | ✅ |
| Container Escape | Privileged pod → host filesystem mount | ✅ |
| RBAC Escalation | Service account token → cluster enumeration | ✅ |
| Secrets Extraction | Plaintext ENV var credential dump | ✅ |

## Phase 3 — Detection & Defense

Deployed a full defense layer across the cluster.

| Tool | Purpose | Result |
|------|---------|--------|
| Tetragon | eBPF runtime detection — every syscall monitored | ✅ |
| OPA Gatekeeper | Privileged pods blocked | ✅ |
| OPA Gatekeeper | Unknown registries blocked | ✅ |
| Network Policies | Default deny + namespace isolation | ✅ |
| Auto-remediation | Suspicious pod auto-kill scripts | ✅ |
| Kubescape | Cluster security scan — 75/100 | ✅ |

**Kubescape Compliance:**
- MITRE ATT&CK: 67.89%
- NSA Kubernetes Hardening: 65.90%

## Phase 4 — Hardening & Automation *(Coming Soon)*

- CI/CD security pipeline
- Makefile automation
- Full hardening based on Kubescape findings
