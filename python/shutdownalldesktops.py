import paramiko

def shutdown_all_systems(host):
    command = "shutdown -s -t 00"

    # Update the next three lines with your
    # server's information

    host = host
    username = "admin"
    password = "$vkM@2022"

    try:
        client = paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password)
        _stdin, _stdout,_stderr = client.exec_command(command)
        print(_stdout.read().decode())        
        client.close()
    except:
        print(f"{host} not reachable ")

def shutdown_select_systems(host):
    command = "shutdown -s -t 00"

    # Update the next three lines with your
    # server's information

    host = host
    username = "admin"
    password = "$vkM@2022"

    try:
        client = paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password)
        _stdin, _stdout,_stderr = client.exec_command(command)
        print(_stdout.read().decode())        
        client.close()
    except:
        print(f"{host} not reachable ")        
    

MY_HOSTS = ['SIRCC1-01152022', 'SIRCC1-02152022', 'SIRCC1-03152022', 'SIRCC1-04152022', 'SIRCC1-05152022', 'SIRCC1-06152022', 'SIRCC1-07152022', 'SIRCC1-08152022', 'SIRCC1-09152022', 'SIRCC1-10152022', 'SIRCC1-11152022', 'SIRCC1-12152022', 'SIRCC1-13152022', 'SIRCC1-14152022', 'SIRCC1-15152022', 'SIRCC1-16152022', 'SIRCC1-17152022', 'SIRCC1-18152022', 'SIRCC1-19152022', 'SIRCC1-20152022', 'SIRCC1-21152022', 'SIRCC1-22152022', 'SIRCC1-23152022', 'SIRCC1-24152022', 'SIRCC1-25152022', 'SIRCC1-26152022', 'SIRCC1-27152022', 'SIRCC1-28152022', 'SIRCC1-29152022', 'SIRCC1-30152022', 'SIRCC1-31152022', 'SIRCC1-32152022', 'SIRCC1-33152022', 'SIRCC1-34152022', 'SIRCC1-35152022', 'SIRCC1-36152022', 'SIRCC1-37152022', 'SIRCC1-38152022', 'SIRCC1-39152022', 'SIRCC1-40152022', 'SIRCC1-41152022', 'SIRCC1-42152022', 'SIRCC1-43152022', 'SIRCC1-44152022', 'SIRCC1-45152022', 'SIRCC1-46152022', 'SIRCC1-47152022', 'SIRCC1-48152022', 'SIRCC1-49152022', 'SIRCC1-50152022', 'SIRCC1-51152022', 'SIRCC1-52152022', 'SIRCC1-53152022', 'SIRCC1-54152022', 'SIRCC1-55152022', 'SIRCC1-56152022', 'SIRCC1-57152022', 'SIRCC1-58152022', 'SIRCC1-59152022', 'SIRCC1-60152022']

all = input("Do you want shutdown all systems, press y or n: ")

if all == 'y':
    for host in MY_HOSTS:
        host = host + '.local'    
        shutdown_all_systems(host)
elif all == 'n':
    which_pc = input("Enter the systems numbers with comma in between e.g. 1,2,3: ")
    which_pc = which_pc.split(',')
    print(which_pc)
    for h in which_pc:
        host = MY_HOSTS[int(h)-1]
        host = host + ".local"
        shutdown_select_systems(host)    

"""
for host in MY_HOSTS:
    host = host + '.local'    
    connect_remote_system(host)
"""        
