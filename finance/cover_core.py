import hashlib
import time
import functools
import datetime
import threading
import os
from gatekeeper import FinanceGatekeeper

# --- 1. CONFIGURATION ---
# Replace with your actual QuickNode URL
RPC_URL = "YOUR_ACTUAL_QUICKNODE_RPC_URL"
gk = FinanceGatekeeper(rpc_url=RPC_URL, budget_limit=0.005)

# --- 2. THE WATCHTOWER (Observer) ---
def start_watchtower():
    """Continuously monitors the ledger for BLOCKED status."""
    ledger_path = "../clover_ledger.md"
    last_size = os.path.getsize(ledger_path) if os.path.exists(ledger_path) else 0
    
    while True:
        if os.path.exists(ledger_path):
            current_size = os.path.getsize(ledger_path)
            if current_size > last_size:
                with open(ledger_path, "r") as f:
                    f.seek(last_size)
                    content = f.read()
                    if "BLOCKED" in content:
                        print(f"\n[!!! WATCHTOWER ALERT !!!]: {content.strip()}")
                last_size = current_size
        time.sleep(5)

# --- 3. THE TRINITY CORE (Architecture) ---
def require_weightless_fee(func):
    """Gatekeeper Decorator: Validates before broadcast."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        live_fee = gk.fetch_live_fee()
        is_valid = gk.evaluate_fee(live_fee)
        
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "VALIDATED" if is_valid else "BLOCKED_EXCEEDS_BUDGET"
        log_entry = f"[{timestamp}] FINANCE_CHECK | FEE: {live_fee} | STATUS: {status}\n"
        
        with open('../clover_ledger.md', 'a') as f:
            f.write(log_entry)
            
        if is_valid:
            return func(*args, **kwargs)
        return None
    return wrapper

@require_weightless_fee
def perform_heartbeat():
    """The protected core action."""
    pulse = f"HB_{time.time_ns()}"
    proof = hashlib.sha256(pulse.encode()).hexdigest()
    print(f"[TRINITY]: Heartbeat broadcast: {proof[:8]}...")
    return True

# --- 4. EXECUTION LAYER ---
if __name__ == "__main__":
    print("Trinity Core + Watchtower Initialized.")
    
    # Start Watchtower as background thread
    wt = threading.Thread(target=start_watchtower, daemon=True)
    wt.start()
    
    # Run core logic in main loop
    while True:
        perform_heartbeat()
        time.sleep(60) # Interval of 60 seconds

