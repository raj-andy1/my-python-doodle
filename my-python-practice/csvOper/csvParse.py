import pandas as pd
import re


def getresults(csv_in_file, plugin_id, results_out_csvfile, exclude_controls=None):
    rule_set = set()
    df = pd.read_csv(csv_in_file, low_memory=False, usecols=['Host', 'Description', 'Plugin ID'])
    filtered_result = df[df['Plugin ID'].isin([plugin_id])].reset_index(drop=True)
    '''
    pattern = r'(UBTU-\d+-\d+) .*: \[([A-Z]+)\]'
    filtered_result[['RuleId', 'Result']] = filtered_result['Description'].str.extract(pattern)
    '''
    pattern = r'(UBTU-\d+-\d+) - (.*): \[([A-Z]+)\]'
    filtered_result[['RuleId', 'Description', 'Result']] = filtered_result['Description'].str.extract(pattern)
    # filtered_result = filtered_result[filtered_result['Host'].isin(host_ids)].reset_index(drop=True)
    final_result = filtered_result.drop(columns=['Plugin ID'])
    if exclude_controls:
        final_result = final_result[~final_result['RuleId'].isin(exclude_controls)]
    final_result.to_csv(results_out_csvfile, index=False)
    return True


def get_hosts(csv_in_file):
    df = pd.read_csv(csv_in_file, low_memory=False, usecols=['Host'])
    hosts = set(df['Host'].unique())
    return hosts


def getRDSResults(csv_in_file, plugin_id, exclude_controls=None):
    df = pd.read_csv(csv_in_file, low_memory=False, usecols=['Host', 'Description', 'Plugin ID'])
    filtered_result = df[df['Plugin ID'].isin([plugin_id])].reset_index(drop=True)
    # Define the pattern to match the error details
    pattern = r'Error:\n(.*):\n  ERROR: (.*)'

    # Apply the pattern to the 'Description' column
    filtered_result[['ErrorId', 'ErrorDetails']] = filtered_result['Description'].str.extract(pattern, expand=True)


    # Print the DataFrame to check the result
    print(filtered_result)


def main():
    """
    getresults('andyr_agent_ubuntu_os.csv',
               21157,
               'Compliance_Scan2.csv')

    print(get_hosts('Baseline_Agent_Scan_-_VULN.csv'))
    """
    getRDSResults('Test RDS Scan - apd-luigi-prod-fedm-east-luigi-dedicated-rds.ctg7hqh2vrv9.us-east-1.rds.amazonaws.com.csv',
                  148944
            )

if __name__ == '__main__':
    main()
