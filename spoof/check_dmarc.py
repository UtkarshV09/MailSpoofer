import checkdmarc
import dns.resolver


class Dmarc:
    def __init__(self, domain):
        self.domain = domain
        self.resolver = dns.resolver.Resolver()
        self.resolver.nameservers = ['8.8.8.8']

    def check_domain(self):
        try:
            result = checkdmarc.get_dmarc_record(self.domain, resolver=self.resolver)
            result_string = "\n".join(f"{k}: {v}" for k, v in result.items())
            return result_string
        except checkdmarc.DMARCRecordNotFound as e:
            print(f"No Dmarc record found for {self.domain} {e}")
        except Exception as e:
            print(f"An Error occurred while checking: {e}")
            return None


