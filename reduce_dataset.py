import os
import random

# Paths to your six folders
folders = [
    "/Users/maanas/Downloads/Dataset/Train/Real",
    "/Users/maanas/Downloads/Dataset/Train/Fake",
    "/Users/maanas/Downloads/Dataset/Test/Real",
    "/Users/maanas/Downloads/Dataset/Test/Fake",
    "/Users/maanas/Downloads/Dataset/Validation/Real",
    "/Users/maanas/Downloads/Dataset/Validation/Fake"
]

# Function to ensure each folder has exactly 20000 image files
def ensure_folder_has_20000(folder):
    # Get only image files (ending in .jpg, .jpeg, .png, etc.), skip folders and hidden files
    image_extensions = ('.jpg', '.jpeg', '.png')
    files = [f for f in os.listdir(folder) if f.lower().endswith(image_extensions) and not f.startswith('.')]
    
    if not files:
        print(f"No image files found in {folder}")
        return
    
    total_files = len(files)
    
    if total_files > 20000:
        # Reduce files to 20000 by randomly deleting excess files
        files_to_delete = total_files - 20000
        files_to_remove = random.sample(files, files_to_delete)
        for file in files_to_remove:
            file_path = os.path.join(folder, file)
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except PermissionError:
                print(f"Couldn’t delete {file_path} - Permission denied, skipping")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}, skipping")
        print(f"Reduced {folder} from {total_files} to 20000 image files")
    
    elif total_files < 20000:
        print(f"{folder} has only {total_files} images, consider adding more")
    else:
        print(f"{folder} already has exactly 20000 images, no changes needed")

# Loop through all folders and process them
for folder in folders:
    if os.path.exists(folder):
        print(f"Processing {folder}...")
        ensure_folder_has_20000(folder)
    else:
        print(f"Folder not found: {folder}")

print("Dataset processing complete: Each folder now has exactly 20000 images (if possible)")
