# file_upload_validation(vuln).py

import os

def upload_file(file_name):
    # Create uploads folder if not exists
    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    with open(f"uploads/{file_name}", "wb") as f:
        f.write(b"<?php echo 'hacked'; ?>")

upload_file("shell.php")
