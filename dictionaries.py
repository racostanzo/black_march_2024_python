import os

def generate_file_info():
    files_info = []
    for filename in os.listdir():
        if os.path.isfile(filename):
            file_stat = os.stat(filename)
            file_info = {
                "filename": filename,
                "size": file_stat.st_size,
                "last_modified": file_stat.st_mtime
            }
            files_info.append(file_info)
    return files_info

if __name__ == "__main__":
    files_info = generate_file_info()
    for file_info in files_info:
        print(file_info)
