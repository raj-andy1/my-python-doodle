

# Open the input file
with open('newFailures.txt', 'r') as file:
    # Read lines from the file
    lines = file.readlines()

# Filter lines starting with "Failed" or "Warning"
filtered_lines = [line.strip() for line in lines if line.startswith("Failed") or line.startswith("Warning")]

# Write the filtered lines to a new file
with open('newFailures1.txt', 'w') as file:
    file.write('\n'.join(filtered_lines))
