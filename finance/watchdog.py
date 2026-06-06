import os
import time

def check_trinity():
    while True:
        # Check if the trinity session is running
        if os.popen("tmux ls | grep trinity").read() == "":
            print("[WATCHDOG]: Trinity detected offline. Rebooting...")
            os.system("tmux new -s trinity -d 'python3 ~/my_story_vault/finance/clover_core.py'")
        time.sleep(30)

if __name__ == "__main__":
    check_trinity()

