import json

#firmware counter dictionary that will contain the firmware version as key and count as value
firmware_counter = {}

#not running configured version dictionary that will contain the S/N and URL for devices with firmware not running configured version
not_running_configured_version = {}

# Opening JSON file
f = open('getOrganizationDevices.json', )

# returns JSON object as a dictionary
data = json.load(f)
item = 0
#Tip#1: Use for loop to iterate through json data - for i in data:
print(data)
for item in data:
    running_firmware = item.get('firmware')

    if running_firmware in firmware_counter:
        counter = firmware_counter[running_firmware] + 1
        firmware_counter[running_firmware] = counter
    else:
        #print(running_firmware)
        firmware_counter[running_firmware] = 1
    if running_firmware == 'Not running configured version':
        serial = item.get('serial')
        url = item.get('url')
        not_running_configured_version[serial]= url

#print(firmware_counter)
#print(not_running_configured_version)






    #Tip#2:  print variable i to get information on the key value pair for the json data. Take note of keys firmware, serial number and url
    #print(i)
    

    #Tip#3: Use if statement to check if firmware exists in firmware_counter dictionary and then add the count. Else, update the dictionary with firmware and 1



    #Tip#4: Use if statement to compare firmware with "Not running configured version" then update the the dictionary with S/N and URl



# Closing file
f.close()

print(firmware_counter)

print(not_running_configured_version)





