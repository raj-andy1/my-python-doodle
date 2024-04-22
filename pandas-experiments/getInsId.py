import pandas as pd
import csv
import re

inst_ids_envoy = ["i-0a64e74abf8c51915", "i-0a49902dc14c119c7", "i-06e7aca21af02992f",
                  "i-059d83bdb1b07e187", "i-010c4aaf9b6749cc4", "i-04bd3f60afe7106cf",
                  "i-0e36e1f8f95c8a739", "i-03d601f09902b11e8", "i-07b9b8587a09f5093",
                  "i-067b648f6f44206f4", "i-0a2d2abfc65baddde", "i-0fac8431720ebfc6e",
                  "i-02ea1f6246b039d8b", "i-0a6d563d044843781", "i-0fedc7a25b22094b1",
                  "i-05eb135a552de0cbd", "i-0e0d8f7ccda4f3059", "i-01ffd9f286ce736a6",
                  "i-0d2daec78416d1582", "i-0e11b6f0f2e90473c", "i-0e40cef57c4785a4d",
                  "i-0ab61525a6f24de55", "i-0295f82d0c93fbbfa", "i-0607e805aa42ac997",
                  "i-0adf7b6d16fbf14a6", "i-0fa6046b8ac804c1b", "i-08cf44a0cbbb51920",
                  "i-0e79c9acc7fc978ca", "i-0a466218a88543ec8"]

inst_ids_burp = ["i-0e357e5f8dc4e71ec", "i-0e2ba5593bdec2d6a"]
inst_ids_cloudsec = ["i-0060dc77c298960a1",
                     "i-0b2777c8cc0188703",
                     "i-0e6854c35a0a9adc5",
                     "i-0f6ca7006e2eda927",
                     "i-0f40c5209682508e3",
                     "i-0ef88002d6dc3335c",
                     "i-0dc6ee2360c786382",
                     "i-00d3f84cdec8f77f0",
                     "i-0bd14d6e879b15e60",
                     "i-0f30c1326ae8a0316"]
inst_ids_cloudsec_fixtures = ['i-099e9cdf78ba139a3',
                              'i-0a9225e15847e1513',
                              'i-065b59439f62ba545',
                              'i-0b1a75344d2cd0315',
                              'i-040712fef960d3396',
                              'i-06cfc4ee70f831215',
                              'i-0b1c34311cb83839b',
                              'i-0b9073fe6cc47e328',
                              'i-08dcb6083d09739d3',
                              'i-0f0137429395a1613',
                              'i-0e84ee735b6085187',
                              'i-060ac6aa882e97ada']


class GetInst:

    def __init__(self, csv_in_file):
        self.csv_in_file = csv_in_file
        pass

    def filterresults(self, plugin_id, csv_out_file):
        """
        filter the results based on the plugin id
        """
        df = pd.read_csv(self.csv_in_file, low_memory=False)
        filtered_df = df[df['Plugin ID'] == plugin_id]
        filtered_df.to_csv(csv_out_file, index=False)
        # print(df.columns.values.tolist())
        return True

    @staticmethod
    def checkhostid(csv_in_file, list_input):
        df = pd.read_csv(csv_in_file, low_memory=False)
        instId = set()
        for index, row in df.iterrows():
            instId.add(row['Host'])
        print(len(instId))
        return instId & set(list_input)

    def getresults(self, plugin_id, results_out_csvfile, host_ids=None, exclude_controls=None):
        df = pd.read_csv(self.csv_in_file, low_memory=False, usecols=['Host', 'Description', 'Plugin ID'])
        pattern = r'(\d+\.\d+) (.*?): \[([A-Z]+)\]'
        filtered_result = df[df['Plugin ID'].isin([plugin_id])].reset_index(drop=True)
        filtered_result[['RuleId', 'Desc', 'Result']] = filtered_result['Description'].str.extract(pattern)
        filtered_result = filtered_result[filtered_result['Host'].isin(host_ids)].reset_index(drop=True)
        final_result = filtered_result.drop(columns=['Description', 'Plugin ID'])
        final_result = final_result[~final_result['RuleId'].isin(exclude_controls)]
        final_result_failed = final_result[final_result['Result'].isin(['FAILED'])]
        final_result_failed.to_csv(results_out_csvfile, index=False)
        return True


def main():
    inst_docker = GetInst(csv_in_file='/Users/arajagopalan/Downloads/Baseline_Agent_Scan_-_Docker (3).csv')
    inst_ubuntu = GetInst(csv_in_file='/Users/arajagopalan/Downloads/Baseline_Agent_Scan_-_Ubuntu_20 (4).csv')
    inst_docker.getresults(21157,
                           host_ids=['i-01204664c748902bb',
                                     'i-0807f3542d367bc85'],
                           results_out_csvfile='results_docker.csv',
                           exclude_controls=['2.1', '2.2', '2.7', '2.9', '2.12', '2.15', '3.9', '3.10',
                                             '3.11', '3.12', '3.13', '4.11', '5.2', '5.3', '5.11', '5.12',
                                             '5.26', '5.29', '5.31', '7.1', '7.2', '7.3', '7.5', '7.6',
                                             '7.7', '7.8', '7.9', '7.10'])
    inst_ubuntu.getresults(21157,
                           'results_ubuntu.csv')


if __name__ == "__main__":
    main()
