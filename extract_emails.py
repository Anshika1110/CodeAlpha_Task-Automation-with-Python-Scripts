import os
import re

# Input and output file names
input_file = "input.txt"
output_file = "emails.txt"

# Regular expression for email pattern
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Check if the input file exists
if not os.path.exists(input_file):
    print(f"❌ Error: The file '{input_file}' does not exist.")
else:
    # Read the input file
    with open(input_file, 'r') as file:
        content = file.read()

    # Extract emails using regex
    emails = re.findall(email_pattern, content)
    unique_emails = sorted(set(emails))  # remove duplicates and sort

    # Write to the output file
    with open(output_file, 'w') as file:
        for email in unique_emails:
            file.write(email + '\n')

    print(f"✅ Extraction complete. {len(unique_emails)} email(s) saved to '{output_file}'.")
