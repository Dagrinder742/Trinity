
























def run_stress_test(iterations=10000):
    key_history = {}
    
    for i in range(iterations):
        # Your 4-state inputs (0-3) mapped to a dice roll
        # We simulate the "Back to Front" logic
        dice_roll = (i % 36) + 1
        resonance = 4.5
        jump_factor = 25
        
        # The core Trinity Equation
        key = int((dice_roll * resonance * jump_factor) % 99)
        
        # Audit the key
        key_history[key] = key_history.get(key, 0) + 1
        
    # Analyze distribution
    unique_keys = len(key_history)
    print(f"--- TRINITY PROTOCOL AUDIT ---")
    print(f"Total Transactions: {iterations}")
    print(f"Keys Hit: {unique_keys}/99")
    print(f"Audit Status: {'STABLE' if unique_keys > 30 else 'DRIFT DETECTED'}")

run_stress_test()
def run_tripled_stress_test(iterations=10000):
    key_history = {}
    
    for i in range(iterations):
        # 3-Roll Triangulation
        r1 = (i % 36) + 1
        r2 = ((i * 5) % 36) + 1 # The x5 scaling sequence
        r3 = ((i * 25) % 36) + 1 # The 5x5 expansion
        
        # Triangulated Dice Result (Harmonic Average)
        dice_avg = (r1 + r2 + r3) / 3
        
        # Trinity Resonance calculation (4.5 median)
        # Using the Back-to-Front inversion logic
        raw_key = int((dice_avg * 4.5 * 25) % 99)
        key_index = (99 - raw_key) % 99
        
        # Log the hit
        key_history[key_index] = key_history.get(key_index, 0) + 1
        
    unique_keys = len(key_history)
    print(f"--- TRINITY PROTOCOL: TRIPLE-ROLL AUDIT ---")
    print(f"Unique Keys Hit: {unique_keys}/99")
    print(f"Status: {'STABLE' if unique_keys > 70 else 'DRIFT DETECTED'}")

run_tripled_stress_test()
