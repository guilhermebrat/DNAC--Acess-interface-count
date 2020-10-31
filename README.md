# DNAC--Acess-interface-count
The objective of this script is to get the status of all user interfaces(Gigabit) in the DNA-C infrastructure.
Note that the code is still hard-coded to get only equipement that the role is "Access"

## Use Case Description

This script was written on my use case, after the company has moved to a new building we lost track how many interfaces were used regarding the number of network jacks installed.
The idea is to easily way to get which switches has interfaces available without checking each device and avoiding spreadsheets.

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
`connect_dnac.py` contains the : dna url, username and password
  
  Before you start to use it, you need to change for the credentials of you DNA-C.
  
  
![connect_dna](https://user-images.githubusercontent.com/25211596/97782564-8f520d00-1b68-11eb-81a4-9af60a57939e.PNG)

## Usage
After updating the credentials on the `connect_dnac.py`, run the  `get_interfaces.py`

Here is the test using the DevNet Sandbox

### Obs: 
The reason that it shows only interfaces down on the sandbox because the hosts are connected using the 'TenGigabit" interfaces but we are only checking for 'Gigabit'.

The code that filters by GigabitEthernet

![image](https://user-images.githubusercontent.com/25211596/97790863-d78e2100-1ba2-11eb-91b5-3020b7c90e7c.png)

The result:

![image](https://user-images.githubusercontent.com/25211596/97790814-546ccb00-1ba2-11eb-9b23-6996c816f0f5.png)

If we change our Script to look for `TenGigabitEthernet` 

![image](https://user-images.githubusercontent.com/25211596/97790833-8c740e00-1ba2-11eb-8148-51265f6a29db.png)

We will receive the following output

![image](https://user-images.githubusercontent.com/25211596/97790844-9dbd1a80-1ba2-11eb-8687-bfffdb78b5a8.png)

## Next Steps

Its not perfect and has lots of room for improvement but we can achieve our primary goal

* Gather all interfaces and displays the types on the table
* User selection type of device, Access, Border or Core
