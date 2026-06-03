import hashlib
import sys

# THE GODFATHER: Auditor and Gatekeeper
def godfather_supervisor(input_data, registry):
    # Generates hash of input and audits against the "Source of Truth"
    line_hash = hashlib.sha256(input_data.strip().encode()).hexdigest()

    if line_hash in registry:
        print(f"[GODFATHER_VERIFIED]: {line_hash[:16]}...")
        return True
    else:
        print(f"[GODFATHER_ALERT]: Integrity Breach - Hash {line_hash[:16]} unrecognized.")
        return False

if __name__ == "__main__":
    # Load registry and process input
    try:
        with open('registry.txt', 'r') as f:
            registry = set(line.strip() for line in f)

        input_stream = sys.argv[1] if len(sys.argv) > 1 else ""
        if not godfather_supervisor(input_stream, registry):
            sys.exit(1)
    except FileNotFoundError:
        print("[GODFATHER_ERROR]: registry.txt not found. Protocol sealed.")
        sys.exit(1)
