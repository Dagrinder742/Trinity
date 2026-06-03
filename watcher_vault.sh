#!/bin/bash
# Absolute paths to ensure consistency
LEDGER="/data/data/com.termux/files/home/my_story_vault/data/ledger.bin"
ENGINE="/data/data/com.termux/files/home/my_story_vault/vault_engine"

echo "--- TRINITY SECURITY MONITOR: ACTIVE ---"

# The 'while' loop keeps the process alive
while true; do
    # inotifywait watches for the 'modify' event on the ledger
    inotifywait -q -e modify "$LEDGER" > /dev/null
    
    echo -e "\n[!] ALERT: Ledger modification detected. Initiating Integrity Scan..."
    
    # Run the engine and check if it returns a non-zero exit code (failure)
    if ! "$ENGINE"; then
        echo "[!!!] GOVERNANCE BREACH: Engine rejected ledger state."
    else
        echo "[+] INTEGRITY VERIFIED: Ledger state is consistent."
    fi
done

