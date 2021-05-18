cases = ["123", "1023", "90123", "1231", "123123", "123123123123"]


def print_valid_ips(str):
    print ('str {}'.format(str))
    print ('****')
    for i in range (1, len(str)-2):
        for j in range (i, len(str)-1):
            for k in range (j, len(str)):
                parts = [str[0:i], str[i:j], str[j:k], str[k:len(str)]]
        print (parts)

for case in cases:
    print_valid_ips(case)