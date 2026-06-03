#!/usr/bin/env python3o

# Your actual script code goes here
4.  Press **Ctrl + O**, then **Enter** to save, and **Ctrl + X** to exit nano.

### 2. Move the File
Now that the file content is correct, run these commands one by one to put it in the right place:

*   **Make the directory:** `mkdir -p ~/.local/bin`
*   **Move the file:** `cp TrinityProtocol.py ~/.local/bin/TrinityProtocol`
*   **Make it executable:** `chmod +x ~/.local/bin/TrinityProtocol`

### 3. Add to PATH
You need to make sure the terminal knows to look in that folder.

1.  Open your shell config: `nano ~/.bashrc`
2.  Go to the very bottom of the file and add this line:
    ```bash
    export PATH=$PATH:~/.local/bin
