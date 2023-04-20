from wakeonlan import send_magic_packet
# List of 60 MAC Addresses
mac_list = ['38-CA-84-49-95-70', '38-CA-84-4C-7C-F2', '38-CA-84-49-A5-78', '38-CA-84-4B-1E-A3', '38-CA-84-49-35-BE', '38-CA-84-4C-31-70', '38-CA-84-4C-78-C3', '38-CA-84-4C-D8-75', '38-CA-84-49-E1-97', '38-CA-84-4A-CC-DE', '38-CA-84-4C-C0-4D', '38-CA-84-4C-C8-66', '38-CA-84-4C-7C-DD', '38-CA-84-4C-7C-9C', '38-CA-84-4C-58-D9', '38-CA-84-4C-55-36', '38:ca:84:4a:4a:bf', '38-CA-84-4C-21-5B', '38-CA-84-4C-18-88', '38-CA-84-49-E1-BA', '38-CA-84-4C-9C-66', '38-CA-84-49-E4-D9', '38-CA-84-4C-31-57', '38-CA-84-4C-1D-2B', '38-CA-84-4C-68-5C', '38-CA-84-4A-9F-11', '38-CA-84-4C-FA-F7', '38-CA-84-4C-E8-D9', '38-CA-84-4C-8C-C4', '38-CA-84-4C-A8-2D', '38-CA-84-4B-AF-5A', '38-CA-84-4C-18-65', '38-CA-84-4C-80-57', '38-CA-84-4C-7C-01', '38-CA-84-4C-01-21', '38-CA-84-4C-08-40', '38-CA-84-4C-08-01', '38-CA-84-4A-DC-A6', '38-CA-84-4C-C8-71', '38-CA-84-4C-07-67', '38-CA-84-49-91-76', '38-CA-84-4C-7C-E0', '38-CA-84-4B-9F-EC', '38-CA-84-4C-98-BC', '38-CA-84-4B-2F-A5', '38-CA-84-4C-68-4A', '38-CA-84-4C-08-45', '38-CA-84-4C-98-77', '38-CA-84-4B-AE-67', '38-CA-84-4C-18-A1', '38-CA-84-4B-5E-86', '38-CA-84-4C-55-AE', '38-CA-84-4C-98-2C', '38-CA-84-4C-36-C5', '38-CA-84-4A-EC-D1', '38-CA-84-49-91-7E', '38-CA-84-4A-0D-57', '38-CA-84-4C-17-59', '38-CA-84-4C-78-A0', '38-CA-84-4C-C8-8F']

# Taking input to start particular desktops from above list
start_which_pc = input("Enter PC number you want to start e.g. 1,2,3,60: ")

# Splitting input using ',' delimeter
pc_start_list = start_which_pc.split(",")

# Running for loop to interate throgh start pc list and accessing MAC accordingly
for pc in pc_start_list:
    send_magic_packet(mac_list[int(pc) - 1])
