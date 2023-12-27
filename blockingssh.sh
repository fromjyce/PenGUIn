#!/bin/bash



# Block incoming SSH traffic
sudo iptables -A INPUT -p tcp --dport 22 -j DROP

# Save the rules
sudo iptables-save > /etc/iptables/rules.v4
