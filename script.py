import os
from PIL import Image
from tqdm import tqdm

input_dir = r'' # Specify the input directory containing JPG files
output_dir = r'' # Specify the output directory for compressed images
max_size = (3000, 2000)

os.makedirs(output_dir, exist_ok=True)
jpg_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.jpg')]

for filename in tqdm(jpg_files, desc="Compressing images"):
    img_path = os.path.join(input_dir, filename)
    img = Image.open(img_path)
    img.thumbnail(max_size, Image.LANCZOS)
    output_path = os.path.join(output_dir, filename)
    img.save(output_path, 'JPEG', quality=85, optimize=True)