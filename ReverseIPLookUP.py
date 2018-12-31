########################
## Reverse IP LookUp  ##
# Extract all domains  #
#       9aylas         #
########################

import requests
api = "http://api.hackertarget.com/reverseiplookup/"
x = raw_input(" Enter IP : ")
ip = {"q":x}
pwn = requests.request("GET", api, params=ip)
print(pwn.text)

r = raw_input("* Wanna save this result to a text file ? Y/N \n ~ ")
if r == "Y" or r == "y":
	file = open("dumped.txt","w") 
	file.write(pwn.text)
	file.close()
else:
	print(" Bye ^_^ ")