import functools
from gatekeeper import FinanceGatekeeper

# Initialize the gatekeeper (ensure your RPC URL is set)
gk = FinanceGatekeeper(rpc_url="YOUR_QUICKNODE_RPC_URL", budget_limit=0.005)

def require_weightless_fee(func):
    """Decorator to ensure every transaction is checked against the Finance Floor."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("[FINANCE]: Transaction requested. Checking Gatekeeper...")
        live_fee = gk.fetch_live_fee()
        
        if gk.evaluate_fee(live_fee):
            print(f"[FINANCE]: Fee {live_fee} is Weightless. Proceeding.")
            return func(*args, **kwargs) # Broadcast allowed
        else:
            print(f"[FINANCE]: Fee {live_fee} exceeds budget. BROADCAST ABORTED.")
            return None # Broadcast strictly blocked
    return wrapper

# Apply to your signing function
@require_weightless_fee
def sign_and_broadcast_transaction(tx_data):
    # Your original signing and broadcasting logic here
    print("[CORE]: Signing and broadcasting to blockchain...")

