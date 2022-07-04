# Author: 9aylas
# Version: 1.2
# Licence: MIT
# Update: July 2022 (Contributor: C3n7ral051nt4g3ncy)

# Python Libraries
import requests
import time
import sys


# Reverse IP lookup Python Tool using the Hacker Target API to extract all domains with the same IP address
print("""
#############################
##    Reverse IP LookUp    ##
#    Extract all domains    #
#          9aylas           #
# https://github.com/9aylas #
#       Licence: MIT        #
#############################""")
time.sleep(3)


# Reverse IP search using Hacker Target free API (Limited use)
def reverse_ip_free():
    """
    Reverse IP Search
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

	
	
def main():
        reverse_ip_free()
	
	
	


if __name__ == '__main__':
    main()
