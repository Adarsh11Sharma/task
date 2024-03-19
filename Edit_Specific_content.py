def change_content(file_path, old_content, new_content):
    try:
        # Read the content of the file
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Replace the specific content with the new content
        modified_content = content.replace(old_content, new_content)
        
        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(modified_content)
        
        print("Content changed successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"Error occurred: {e}")

def main():
    file_path = input("Enter the path to the text file: ")
    old_content = input("Enter the content you want to replace: ")
    new_content = input("Enter the new content: ")
    
    change_content(file_path, old_content, new_content)

if __name__ == "__main__":
    main()
