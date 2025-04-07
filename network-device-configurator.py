from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.10",
    "username": "admin",
    "password": "yourpassword",
}

commands = ["hostname Router1", "no ip domain-lookup"]

connection = ConnectHandler(**device)
output = connection.send_config_set(commands)
print(output)

connection.disconnect()
