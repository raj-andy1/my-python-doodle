import pandas as pd
import re

csv_in_file = "Jira.csv"

df = pd.read_csv(csv_in_file, low_memory=False)
selected_columns = df.filter(items=["Summary", "IssueKey", "Assignee", "Description",
                                    "Custom field (Asset Type)"])


main_pattern = r'\*Non-Compliant Controls\*:\s*(.*?)\s*\*Non-Compliant Resources\*'
control_pattern = r'\s*(\S+)\s*-\s*(.*)'

# Function to extract control IDs and descriptions from the "Description" column
def extract_controls(description):
    match = re.search(main_pattern, description, re.DOTALL)
    if match:
        extracted_text = match.group(1).strip()
        controls = extracted_text.splitlines()

        # Process each control, removing leading asterisks and splitting by '-'
        cleaned_controls = []
        for control in controls:
            control = control.strip().lstrip('* ').rstrip()
            control_match = re.match(control_pattern, control)
            if control_match:
                control_id, control_desc = control_match.groups()
                cleaned_controls.append([control_id, control_desc])
        return cleaned_controls
    return []

# Apply the function to the "Description" column
selected_columns['Extracted_Controls'] = selected_columns['Description'].apply(extract_controls)

# Expand the extracted controls into separate rows
expanded_controls = selected_columns.explode('Extracted_Controls')

# Split the control ID and description into separate columns
expanded_controls[['Control ID', 'Description']] = pd.DataFrame(expanded_controls['Extracted_Controls'].tolist(), index=expanded_controls.index)

# Drop the 'Extracted_Controls' column (optional)
expanded_controls = expanded_controls.drop(columns=['Extracted_Controls'])

# Show the final DataFrame
print(expanded_controls[['Summary', 'IssueKey', 'Assignee', 'Control ID', 'Description']])
