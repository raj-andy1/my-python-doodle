

class IPAddValidator:

    @staticmethod
    def is_ipadd_valid(ipadd):
        """
        :param ipadd:
        :return:
        """
        is_ipadd_valid = False
        octets = ipadd.split('.')
        if len(octets) == 4:
            for octet in octets:
                if not octet.isdigit() and not(0 <= int(octet) <= 255):
                    print(f"{ipadd} is NOT VALID")
                    break
                else:
                    print(f"{ipadd} is valid")







def main():
    ipvalidate = IPAddValidator()
    ipvalidate.is_ipadd_valid("192.168.1.1")
    ipvalidate.is_ipadd_valid("10.10.101.100")
    ipvalidate.is_ipadd_valid("255.255.255.255")
    ipvalidate.is_ipadd_valid("900.255.255.255")
    ipvalidate.is_ipadd_valid("255.900.255.255")
    ipvalidate.is_ipadd_valid("100.55")


if __name__ == "__main__":
    main()
