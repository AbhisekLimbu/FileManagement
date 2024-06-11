import os
import shutil
from pathlib import Path

# Define the file type categories
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'WordDocuments': ['.doc', '.docx'],
    'PDFs': ['.pdf'],
    'TextFiles': ['.txt'],
    'Spreadsheets': ['.xls', '.xlsx'],
    'Presentations': ['.ppt', '.pptx'],
    'Music': ['.mp3', '.wav', '.aac', '.flac'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Programs': ['.exe', '.msi', '.sh'],
    # Add more categories and file extensions as needed
}

def organize_files(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        
        # Skip directories
        if os.path.isdir(item_path):
            continue
        
        # Determine the file extension
        file_ext = os.path.splitext(item)[1].lower()
        
        # Find the category for the file extension
        category = None
        for cat, exts in FILE_TYPES.items():
            if file_ext in exts:
                category = cat
                break
        
        # If the category is found, move the file to the category folder
        if category:
            category_path = os.path.join(directory, category)
            if not os.path.exists(category_path):
                os.makedirs(category_path)
            
            # Move the file
            shutil.move(item_path, os.path.join(category_path, item))
            print(f"Moved: {item} -> {category}/{item}")

def organize_desktop_and_downloads():
    home = str(Path.home())
    desktop = os.path.join(home, 'Desktop')
    downloads = os.path.join(home, 'Downloads')
    
    print("Organizing Desktop...")
    organize_files(desktop)
    
    print("Organizing Downloads...")
    organize_files(downloads)

if __name__ == "__main__":
    organize_desktop_and_downloads()
