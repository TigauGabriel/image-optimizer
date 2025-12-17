from PIL import Image
import os

# --- CONFIGURATION ---
input_folder = 'input'
output_folder = 'optimized'

def optimize_images():
    # 1. Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output folder: {output_folder}")

    # 2. Check if input folder exists
    if not os.path.exists(input_folder):
        print(f"Error: The folder '{input_folder}' was not found. Please create it and add images.")
        return

    # 3. Process files
    files = os.listdir(input_folder)
    count = 0
    print("Starting image optimization... 🚀\n")

    for file in files:
        # Check for valid image extensions
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
            try:
                img_path = os.path.join(input_folder, file)
                
                # Open image
                with Image.open(img_path) as img:
                    # Convert to RGB (necessary for PNG to JPG conversion)
                    img = img.convert('RGB')
                    
                    # Generate new filename (change extension to .jpg)
                    new_filename = os.path.splitext(file)[0] + ".jpg"
                    save_path = os.path.join(output_folder, new_filename)
                    
                    # Save with optimization (Quality 85 is web standard)
                    img.save(save_path, "JPEG", quality=85, optimize=True)
                
                print(f"✅ Converted: {file} -> {new_filename}")
                count += 1
                
            except Exception as e:
                print(f"❌ Error processing {file}: {e}")

    print(f"\nDone! Optimized {count} images. Check the '{output_folder}' directory.")

if __name__ == '__main__':
    optimize_images()