# Author: 9aylas
# Version: 1.3
# Licence: MIT
# Update: July 2022 (Contributor: C3n7ral051nt4g3ncy)

# Python Libraries
import requests
import time
import sys

# Reverse IP lookup Python Tool using the Hacker Target API to extract all domains with the same IP
print("""
#############################
##    Reverse IP LookUp    ##
#    Extract all domains    #
#          9aylas           #
# https://github.com/9aylas #
#       Licence: MIT        #
#############################""")
time.sleep(3)

print("Python reverse IP lookup tool using the Hacker Target API\n")
time.sleep(1)


def function_choice():

    choice = input ("""Type "F" for free Search or "API" if you have a Hacker Target API Key: """)
    if choice == "F" or choice == "f":
        reverse_ip_free()
    if choice == "API" or choice == "api":
        reverse_ip_with_api()


# Reverse IP search using Hacker Target free API (Limited use)
def reverse_ip_free():
    """
    Reverse IP Search for Free

    """


    api = "http://api.hackertarget.com/reverseiplookup/"
    x = input (" Enter IP : ")
    ip = {"q": x}
    pwn = requests.request("GET", api, params=ip)
    print(pwn.text)


    r = input("* Wanna save this result to a text file ? Y/N \n ~ ")
    if r == "Y" or r == "y":
        file = open("dumped.txt", "w")
        file.write(pwn.text)
        file.close()
        sys.exit(1)

    else:
        print(" Bye ^_^ ")
        sys.exit(1)


# Using your own Hacker Target API to avoid search restrictions
def reverse_ip_with_api():

    query = input("Target IP: ")
    apikey = input("Paste Hacker Target API: ")
    domain_ip = {"q": query}
    api = f"https://api.hackertarget.com/reverseiplookup/?q={query}&apikey={apikey}"
    response = requests.request("GET", api, params=domain_ip)
    print(response.text)

    r = input("* Wanna save this result to a text file ? Y/N \n ~ ")
    if r == "Y" or r == "y":
        file = open("dumped.txt", "w")
        file.write(pwn.text)
        file.close()
        sys.exit(1)

    else:
        print(" Bye ^_^ ")
        sys.exit(1)


def main():
    function_choice()
    reverse_ip_free()
    reverse_ip_with_api()



if __name__ == '__main__':
    main()
