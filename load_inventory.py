import ansible_runner 
import subprocess

# Getting the inventory with ansible_runner
print("\n****Ansible Inventory****")
out, err = ansible_runner.get_inventory(action='list', response_format='json', inventories=['./hosts.yml'])

# Extracting and printing required host information
print("\n****Hosts Information****")
for host, details in out['_meta']['hostvars'].items():
    name = host
    ip_address = details.get('ansible_host', 'N/A')
    group = 'N/A'
    for group_name, group_data in out.items():
        if host in group_data.get('hosts', []):
            group = group_name
            break
    print(f"Name: {name}, IP Address: {ip_address}, Group: {group}")

# Pinging the hosts
print("\n****Pinging the hosts****")
ping_result = subprocess.run("ansible all:localhost -m ping", shell=True, capture_output=True, text=True)
print(ping_result.stdout)