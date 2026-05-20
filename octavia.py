import os

class Octavia:
    def __init__(self, vault_path):
        self.vault_path = vault_path
        print("Octavia Interface: Online.")
        print(f"Connected to Memory Bank: {vault_path}")

    def scan_memories(self):
        files = [f for f in os.listdir(self.vault_path) if f.endswith('.txt')]
        print(f"Accessing {len(files)} stored memories...")
        for file in files:
            print(f" > Processing node: {file}")

# Initialize the interface
octavia = Octavia("./")
octavia.scan_memories()
python3 octavia.py
