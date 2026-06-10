# Auto-remediation PowerShell script
$suspiciousCommands = @("nmap", "masscan", "netcat", "chmod 777", "cat /etc/shadow", "/etc/shadow")
$namespaces = @("vuln-apps", "default")

Write-Host "[$(Get-Date)] Auto-remediation started..." -ForegroundColor Green

while ($true) {
    foreach ($ns in $namespaces) {
        $pods = kubectl get pods -n $ns --no-headers -o custom-columns=":metadata.name" 2>$null
        
        foreach ($pod in $pods) {
            # Get recent Tetragon events
            $events = kubectl exec -n defense daemonset/tetragon -- `
                tetra getevents -o compact 2>$null | Select-String $pod | Select-Object -Last 10
            
            foreach ($cmd in $suspiciousCommands) {
                if ($events -match [regex]::Escape($cmd)) {
                    Write-Host "[$(Get-Date)] ALERT: '$cmd' detected in pod $pod (ns: $ns)" -ForegroundColor Red
                    Write-Host "[$(Get-Date)] ACTION: Deleting pod $pod..." -ForegroundColor Yellow
                    kubectl delete pod $pod -n $ns
                    Write-Host "[$(Get-Date)] Pod $pod deleted." -ForegroundColor Green
                }
            }
        }
    }
    Write-Host "[$(Get-Date)] Scan complete. Waiting 30s..." -ForegroundColor Cyan
    Start-Sleep -Seconds 30
}