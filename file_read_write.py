# File Read & Write Challenge + Error Handling Lab

def process_file():
    # Ask the user for a filename
    filename = input("Enter the filename to read: ")

    try:
        # Try opening the file for reading
        with open(filename, "r") as infile:
            content = infile.read()

        # Modify content (example: convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f" Successfully created {new_filename} with modified content.")

    except FileNotFoundError:
        print(" Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print(" Error: Permission denied. Cannot read the file.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")


# Run the program
if __name__ == "__main__":
    process_file()
