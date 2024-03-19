import os

def get_files_info(directory):
    files_info = []
    # Get the list of files in the directory
    files = os.listdir(directory)
    for file_name in files:
        file_path = os.path.join(directory, file_name)
        # Checks if it's a file (not a directory)
        if os.path.isfile(file_path):
            # Get file size
            size = os.path.getsize(file_path)
            # Create a dictionary with file information
            file_info = {
                "name": file_name,
                "size": size
            }
            # Add the dictionary to the list
            files_info.append(file_info)
    return files_info

if __name__ == "__main__":
    current_directory = os.getcwd()  # Get the current working directory
    files_info = get_files_info(current_directory)
    print("List of files in the current directory:")
    for file_info in files_info:
        print(file_info)
