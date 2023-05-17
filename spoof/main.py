from check_dmarc import Dmarc
from check_mx_host import CheckMxHost
from check_spf import Spf

domain = input("Enter the domain to check: ")

# Usage:
dmarc_checker = Dmarc(domain)
spf_checker = Spf(domain)
mx_checker = CheckMxHost(domain)

print(f"\n-Here is the DMARC Record for the domain")
print(f"{dmarc_checker.check_domain()}")
print(f"\n-Here is the SPF Record for the domain")
print(f"{spf_checker.check_spf_domain()}")
print(f"\n-Here is the MX Record for the domain")
print(f"{mx_checker.check_mx_hosts()}")
