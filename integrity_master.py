import hashlib
import re

# 1. THE TEACHER: Prunes syntax errors, extra spaces, and ensures clean lines.
def teacher_syntax_cleaner(raw_code):
    # Removes double spaces, fixes punctuation, standardizes lines
    cleaned = re.sub(r'\s+', ' ', raw_code)
    cleaned = cleaned.replace(' .', '.').replace(' ,', ',')
    return cleaned.strip()

# 2. THE SOLDIER: Audits integrity against a "Source of Truth"
def soldier_auditor(cleaned_code, registry):
    current_hash = hashlib.sha256(cleaned_code.encode()).hexdigest()
    if current_hash in registry:
        return True
    return False

# 3. THE GOD FACTOR: Actively monitors the floor
def god_factor_monitor(data_stream, registry):
    for line_id, raw_input in enumerate(data_stream):
        # Teacher cleans it
        clean = teacher_syntax_cleaner(raw_input)
        
        # Soldier verifies it
        if soldier_auditor(clean, registry):
            print(f"[GOD FLOOR ACTIVE]: Line {line_id} Validated.")
        else:
            print(f"[GOD FLOOR ALERT]: Line {line_id} Breach - Status: E")
            # The system halts on breach
            break
