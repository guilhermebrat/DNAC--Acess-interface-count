# This a separate python script that store the username/password
# It uses the DNAC SDK to perform the API calls
import connect_dnac
import json
import time
import calendar
import re
from prettytable import PrettyTable

# The following are calling the connect_dnac script in order to connect to the DNA-C
# Getting the access token
# Getting the list of devices
dna = connect_dnac.connect_dnac()
token = dna.access_token
devices = dna.devices.get_device_list()


# list to be used in the function get_int_count()

list = []

# The purpose of this function is to iterate the devices and retrieve only the Gigabit interfaces
# The idea is to get only the user ports and then count them as up or down


def get_int_count(equipment_id, device_name):

    count_int_up = 0
    count_int_down = 0
    count_int_total = 0
    lista = []


# API GET - get all the interfaces from a device specified by his ID
    get_device_interfaces = dna.devices.get_interface_info_by_id(equipment_id)[
        'response']

    for interface_name in get_device_interfaces:
        if re.match('^GigabitEthernet[1-8]/0', interface_name['portName']) and interface_name['status'] == 'up':

            count_int_up = count_int_up + 1

        elif re.match('^GigabitEthernet[1-8]/0', interface_name['portName']) and interface_name['status'] == 'down':

            count_int_down = count_int_down + 1

    count_int_total = count_int_up + count_int_down
    lista.append(device_name)
    lista.append(count_int_up)
    lista.append(count_int_down)
    lista.append(count_int_total)

    list.append(lista)

# This for iterates all devices that role is "ACCESS" and for each of them calling the function get_int_count()


for device_test in devices['response']:
    if device_test.role == "ACCESS":
        get_int_count(device_test.id, device_test.hostname)

# This function is used to populate the table and display in the console


def print_table(lista_total):
    count_int_up_total = 0
    count_int_down_total = 0
    count_int_total_total = 0
    table = PrettyTable(['Device', 'Ports UP', 'Ports Down', 'Total Ports'])

    for l in lista_total:
        count_int_up_total = count_int_up_total+l[1]
        count_int_down_total = count_int_down_total+l[2]
        count_int_total_total = count_int_total_total+l[3]

    total_list = ['Total', count_int_up_total,
                  count_int_down_total, count_int_total_total]
    lista_total.append(total_list)

    for rec in lista_total:
        table.add_row(rec)

    print(table)


print_table(list)
