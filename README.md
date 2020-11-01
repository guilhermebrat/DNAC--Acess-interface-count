# DNAC-Acess-interface-count
The objective of this script is to get the status of Gigabit all user interfaces in the DNA-C infrastructure.
The script is hard-coded to get only equipement with "Access" role.

## Use Case Description
My company moved to a new building, which made the team lose track of how many interfaces were being used. Hence, the objective of the script is to easily confirm which switches have available interfaces, without having to check for each device. Besides that, we could avoid spreadsheets that were being used for documentation, that were not always kept up to date.

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
The script has two files: connect_dnac.py and get_interfaces.py
`connect_dnac.py` contains the : dna url, username and password
  
Before running the script, the credentials of the DNA-C must be changed.
  
![connect_dna](https://user-images.githubusercontent.com/25211596/97782564-8f520d00-1b68-11eb-81a4-9af60a57939e.PNG)

## Usage
After updating the credentials on the `connect_dnac.py`, run the  `get_interfaces.py`

Here is the test using the DevNet Sandbox.

### Obs: 
The reason why it shows only interfaces down on the sandbox it's because the hosts are connected using the 'TenGigabit" interfaces, but we are only checking for 'Gigabit'.

The code that filters by GigabitEthernet

![image](https://user-images.githubusercontent.com/25211596/97790863-d78e2100-1ba2-11eb-91b5-3020b7c90e7c.png)

The result:

![image](https://user-images.githubusercontent.com/25211596/97790814-546ccb00-1ba2-11eb-9b23-6996c816f0f5.png)

If the script is changed to look for `TenGigabitEthernet` 

![image](https://user-images.githubusercontent.com/25211596/97790833-8c740e00-1ba2-11eb-8148-51265f6a29db.png)

The following output can be observed:

![image](https://user-images.githubusercontent.com/25211596/97790844-9dbd1a80-1ba2-11eb-8687-bfffdb78b5a8.png)

## Next Steps

The primary goal was achieved and it suits the team's needs at the moment. However, the script can be enhanced by applying the programmed next features:

* Gathering all interfaces and displays by the types on the table;
* User selection by Device role, such as Access, Border and/or Core.

## Thank you!
I'd like to thank you for taking the time to check out my project. I'm open to all suggestions and hope that this can be useful to other teams as well.
Thanks!

Guilherme Gianotto Bratfish
guilhermebrat@gmail.com

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/guilhermebrat/DNAC-Acess-interface-count)
