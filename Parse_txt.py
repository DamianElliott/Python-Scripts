import re

# The text file to be parsed
file_name = "example.txt"

# The paragraph to be searched for in the text file
paragraph_to_search = "This is an example paragraph to search for in the text file."

# Open the text file
with open(file_name, "r") as file:
    # Read the file's content
    content = file.read()
    # Use regular expression to search for the paragraph in the text
    match = re.search(paragraph_to_search, content)
    if match:
        print(f"The paragraph was found in {file_name}.")
    else:
        print(f"The paragraph was not found in {file_name}.")
