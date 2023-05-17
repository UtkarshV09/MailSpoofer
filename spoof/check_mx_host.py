import checkdmarc
import dns.resolver


class CheckMxHost:
    def __init__(self, domain):
        self.domain = domain
        self.resolver = dns.resolver.Resolver()
        self.resolver.nameservers = ["8.8.8.8"]

    def check_mx_hosts(self):
        try:
            check_mx_host = checkdmarc.get_mx_hosts(self.domain, resolver=self.resolver)
            check_mx_host_string = "\n".join(f"{k} {v}" for k, v in check_mx_host.items())
            return check_mx_host_string
        except checkdmarc.DMARCReportEmailAddressMissingMXRecords as e:
            print(f" No MX records found for {self.domain} {e}")