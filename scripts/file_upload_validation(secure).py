import mimetypes
import os

def is_safe(file_name, content):
    allowed_mime_types = ['image/jpeg', 'image/png']
    mime_type, _ = mimetypes.guess_type(file_name)
    
    if mime_type in allowed_mime_types and file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
        return True
    return False

def upload_file(file_name, content):
    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    if is_safe(file_name, content):
        with open(f"uploads/{file_name}", "wb") as f:
            f.write(content)
        print("✅ Upload successful.")
    else:
        print("❌ Invalid file type.")

upload_file("shell.php", b"<?php echo 'hacked'; ?>")
