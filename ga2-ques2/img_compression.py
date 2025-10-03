from PIL import Image
from pathlib import Path

input_path = Path("download.png")
output_path = input_path.with_suffix(".webp")
with Image.open(input_path) as img:
    img.save(output_path, "WEBP", lossless=True, optimize=True)

# Now check output file size: it should be <400 bytes
print(output_path.stat().st_size)
