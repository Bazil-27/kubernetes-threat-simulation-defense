#!/bin/bash
# Auto-remediation script
# Monitors Tetragon events and kills suspicious pods

SUSPICIOUS_COMMANDS=("nmap" "masscan" "nc" "netcat" "wget" "curl" "chmod 777" "cat /etc/shadow")
NAMESPACES=("vuln-apps" "default")

echo "[$(date)] Auto-remediation started..."

while true; do
  for ns in "${NAMESPACES[@]}"; do
    pods=$(kubectl get pods -n "$ns" --no-headers -o custom-columns=":metadata.name")
    
    for pod in $pods; do
      # Check Tetragon events for suspicious activity
      events=$(kubectl exec -n defense daemonset/tetragon -- \
        tetra getevents -o compact 2>/dev/null | \
        grep "$pod" | head -5)
      
      for cmd in "${SUSPICIOUS_COMMANDS[@]}"; do
        if echo "$events" | grep -q "$cmd"; then
          echo "[$(date)] ALERT: Suspicious command '$cmd' in pod $pod (ns: $ns)"
          echo "[$(date)] ACTION: Deleting pod $pod..."
          kubectl delete pod "$pod" -n "$ns"
          echo "[$(date)] Pod $pod deleted."
        fi
      done
    done
  done
  sleep 30
done