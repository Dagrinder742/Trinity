def test_resonance(dice_roll):
    # The DDD logic: 3.5 + 1 = 4.5
    resonance = 4.5 
    # Jump Factor (5x5 = 25)
    jump_factor = 25
    # The Roll (Input)
    coordinate = dice_roll * resonance
    # The Mapping (Modulus 99)
    key_index = (coordinate * jump_factor) % 99
    
    print(f"Dice Roll: {dice_roll}")
    print(f"Resonance Point: {key_index}")
    return key_index

# Test the protocol against a dice roll of 36
test_resonance(36)
	
