import base64
import os
import time

def save_base64_image(base64_image: str, upload_folder: str) -> str:
    # Split the base64 data and decode
    header, encoded = base64_image.split(",", 1)
    file_extension = header.split('/')[1].split(';')[0]
    image_data = base64.b64decode(encoded)

    # Create a unique filename with timestamp
    filename = f'image_{int(time.time())}.{file_extension}'
    file_path = os.path.join(upload_folder, filename)

    with open(file_path, 'wb') as f:
        f.write(image_data)

    return filename
