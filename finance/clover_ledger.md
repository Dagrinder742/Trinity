import threading

if __name__ == "__main__":
    # 1. Start the core signing process
    core_thread = threading.Thread(target=run_core_logic, daemon=True)
    core_thread.start()
    
    # 2. Start the watchtower in the same session
    start_watchtower()
import functools
import datetime
from gatekeeper import FinanceGatekeeper

# Initialize the gatekeeper (Ensure rpc_url is correct)
gk = FinanceGatekeeper(rpc_url="YOUR_QUICKNODE_RPC_URL", budget_limit=0.005)

def require_weightless_fee(func):
    """Decorator to gatekeep transactions and log audit trails to the ledger."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Capture the timestamp of the request
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 2. Check the fee via Finance Floor
        live_fee = gk.fetch_live_fee()
        is_valid = gk.evaluate_fee(live_fee)
        
        # 3. Log the audit result to the ledger
        status = "VALIDATED" if is_valid else "BLOCKED_EXCEEDS_BUDGET"
        log_entry = f"[{timestamp}] FINANCE_CHECK | FEE: {live_fee} | STATUS: {status}\n"
        
        with open('../clover_ledger.md', 'a') as f:
            f.write(log_entry)
            
        # 4. Enforce the gate
        if is_valid:
            print(f"[FINANCE]: {status} at {timestamp}. Proceeding.")
            return func(*args, **kwargs)
        else:
            print(f"[FINANCE]: {status} at {timestamp}. Broadcast Aborted.")
            return None
            
    return wrapper

