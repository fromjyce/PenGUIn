#!/bin/bash

# Define the trusted IP range(company's network)
trusted_ip_range="192.168.1.0/24"

# Add iptables rule to allow traffic from the specified IP range
iptables -A INPUT -s "$trusted_ip_range" -j ACCEPT

# Save the iptables rules to persist across reboots
iptables-save > /etc/iptables/rules.v4
