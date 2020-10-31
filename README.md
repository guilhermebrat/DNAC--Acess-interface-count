# DNAC--Acess-interface-count
The objective of this script is to get the status of all user interfaces(Gigabit) in the DNA-C infrastructure.
Note that the code is still hard-coded to get only equipement that the role is "Access"

## Use Case Description

This script was written on my use case, after the company has moved to a new building we lost track how many interfaces were used regarding the number of network jacks installed.
The idea is to be easily and fast way to get which switches has interfaces available.

## Installation
The following libraries are used in this script:

The librarie `connect_dnac` is a second file used to store the username/password/dna-c ip address

 * json
 * time
 * calendar
 * prettytable
 * re
![capture2](https://user-images.githubusercontent.com/25211596/97782733-844bac80-1b69-11eb-9e48-6260dda1cd71.PNG)

## Configuration
The script has two files, connect_dnac.py and get_interfaces.py
`connect_dnac.py` :dnac-c url, username and password
  
  Before you start to use it, you need to change for the credentials of you DNA-C.
  
  
![connect_dna](https://user-images.githubusercontent.com/25211596/97782564-8f520d00-1b68-11eb-81a4-9af60a57939e.PNG)
