#!/usr/bin/python

import os
import sys

IP=raw_input("Enter yr IP:")

def smb_enum():
	try:
		print "[+] smb-user&share enumerating......."
		os.system("nmap -p 445 -vv --script=smb-enum-shares.nse,smb-enum-users.nse",IP)
		print "-----------------------------------"

		print "[+] smb vuln- Scanning ............."
		os.system("nmap -p 445 -vv --script=smb-vuln-cve2009-3103.nse,smb-vuln-ms06-025.nse,smb-vuln-ms07-029.nse,smb-vuln-ms08-067.nse,smb-vuln-ms10-054.nse,smb-vuln-ms10-061.nse,smb-vuln-ms17-010.nse",IP)
		print "------------------------------------"
		print "[+] All smb-Vuln* Checking..........."
		os.system("nmap --script smb-vuln* -p 139,445",IP)

	except Exceptions as error:
		print error
