def read_file(file_path):
    """Read the content of the file."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None

def write_file(file_path, new_content):
    """Write content to the file."""
    try:
        with open(file_path, 'w') as file:
            file.write(new_content)
        print("File updated successfully.")
    except Exception as e:
        print(f"Error occurred while writing to file: {e}")

def main():
    file_path = input("Enter the path to the text file: ")
    content = read_file(file_path)
    if content is not None:
        print("Current content of the file:")
        print(content)
        
        new_content = input("Enter the new content: ")
        
        # Write the new content back to the file
        write_file(file_path, new_content)

if __name__ == "__main__":
    main()