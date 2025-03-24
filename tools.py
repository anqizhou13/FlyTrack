import os

def search_files(directory, search_string):
    matching_files = []
    
    # Walk through all files and subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # Open and read file
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    if search_string in f.read():
                        matching_files.append(file_path)
            except Exception as e:
                print(f"Could not read {file_path}: {e}")
    
    return matching_files
