
# pip install python-whois


import whois


def Domain_info():
    domain = whois.whois(url)
    print(f"Server : {domain.whois_server}")


url = input("Enter URL \n")

try:
    domain = whois.whois(url)
    
except:
    print("This Domain is available")    

else:
    print("This Domain is already purchased")
    print("Domain information \n")
