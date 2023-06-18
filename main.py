
# pip install python-whois


import whois


def Domain_info():
    domain = whois.whois(url)
    print(f"Server : {domain.whois_server}")
    print(f"Expiration Date : {domain.expiration_date}")
    print(f"Name : {domain.name}")
    print(f"Organization : {domain.org}")
    print(f"City : {domain.city}")
    print(f"State : {domain.state}")
    print(f"Country : {domain.country}")






url = input("Enter URL \n")

try:
    domain = whois.whois(url)
    
except:
    print("This Domain is available")    

else:
    print("This Domain is already purchased")
    print("Domain information \n")
