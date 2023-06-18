
# pip install python-whois


import whois


url = input("Enter URL \n")

try:
    domain = whois.whois(url)
    
except:
    print("This Domain is available")    

else:
    print("This Domain is already purchased")