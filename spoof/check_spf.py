import checkdmarc
import dns.resolver


class Spf:
    def __init__(self, domain):
        """Initializing a Spf object"""
        self.domain = domain
        self.resolver = dns.resolver.Resolver()
        self.resolver.nameservers = ["8.8.8.8"]

    def check_spf_domain(self):
        """Check if a domain has SPF  records"""
        try:
            spf_record = checkdmarc.get_spf_record(
                self.domain, resolver=self.resolver, timeout=5.0
            )
            spf_string = "\n".join(f"{k}: {v}" for k, v in spf_record.items())
            return spf_string
        except checkdmarc.SPFRecordNotFound as e:
            print(f"No SPF record found for domain {self.domain}. {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
