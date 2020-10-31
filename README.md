# DNAC--Acess-interface-count
The objective of this script is to get the status of all user interfaces in the DNA-C infrastructure.
Note that the code is still hard-coded to get only equipement that the role is "Access"

Use Case Description
This script was written on my use case, after the company has moved to a new building we lost track how many interfaces were used regarding the number of network jacks installed.
The idea is to be easily and fast way to get which switches has interfaces available.

Installation
The following libraries are used in this script:
#json
#time
#calendar
#prettytable
#re

Configuration
The script has two files, connect_dnac.py and get_interfaces.py
connect_dnac.py :
  Is the file where the, dnac ip/name is configured, username, password.
  Before you start to use it, you need to change for the credentials of you dnac.
  
  
