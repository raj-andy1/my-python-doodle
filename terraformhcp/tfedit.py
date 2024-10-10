import os

def replace_in_file(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()

    # Define the string to search for and the replacement string
    old_string = 'source  = "app.terraform.io/loomhq/route53-zone/aws"\n  version = ">= 1.0.0"'
    new_string = 'source = "../../../modules/aws/route-53-zone"'

    # Check if the old_string exists in the file
    if old_string in file_content:
        # Replace the old string with the new one
        new_content = file_content.replace(old_string, new_string)

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(new_content)

        print(f"Replaced content in: {file_path}")
    else:
        print(f"No replacement needed in: {file_path}")

def find_and_replace_zone_tf(start_dir):
    # Walk through all directories and files recursively
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if file == 'zone.tf':
                # Get the full file path
                file_path = os.path.join(root, file)
                # Perform the replacement operation
                replace_in_file(file_path)

# Replace with the directory you want to start the search from
start_directory = '/Users/arajagopalan/IdeaProjects/infra-terraform/terraform/dns'
find_and_replace_zone_tf(start_directory)
