from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "192.168.50.141",
    "username": "surya",
    "password": "cisco123",       # Update if your password uses a capital 'C'
    "secret": "cisco123",         # Enable secret
    "global_delay_factor": 2,
}

# Establish connection
net_connect = ConnectHandler(**router)
net_connect.enable()

# Execute command and print output
output = net_connect.send_command("show ip int brief")
print(output)

# Close connection cleanly
net_connect.disconnect()