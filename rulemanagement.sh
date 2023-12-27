#!/bin/bash

# Function to check if a package is installed
is_package_installed() {
    dpkg-query -s "$1" &>/dev/null
}

# Function to install a package if not already installed
install_package() {
    if ! is_package_installed "$1"; then
        echo "Installing $1..."
        sudo apt-get install -y "$1"
    fi
}

# Function to enable and start a service
enable_and_start_service() {
    sudo systemctl --now enable "$1"
}

# Function to configure ufw rules for loopback traffic
configure_ufw_loopback() {
    sudo ufw allow in on lo
    sudo ufw allow out on lo
    sudo ufw deny in from 127.0.0.0/8
    sudo ufw deny in from ::1
}

# Function to configure ufw outbound connections
configure_ufw_outbound() {
    sudo ufw allow out on all
}

# Function to configure ufw rules for open ports
configure_ufw_open_ports() {
    open_ports=$(ss -tuln | awk '($5!~/%lo:/ && $5!~/127.0.0.1:/ && $5!~/::1/) {split($5, a, ":"); print a[2]}' | sort | uniq)
    for port in $open_ports; do
        sudo ufw allow in "$port"
    done
}

# Function to set ufw default deny policy
set_ufw_default_deny() {
    sudo ufw default deny incoming
    sudo ufw default deny outgoing
    sudo ufw default deny routed
}

# Main function to perform security configurations
perform_security_configurations() {
    # Install necessary packages for IPtables
    install_package "iptables"
    install_package "iptables-persistent"

    # Configure and save IPv4 rules
    sudo iptables -F
    sudo iptables -P INPUT DROP
    sudo iptables -P OUTPUT DROP
    sudo iptables -P FORWARD DROP
    sudo iptables -A INPUT -i lo -j ACCEPT
    sudo iptables -A OUTPUT -o lo -j ACCEPT
    sudo iptables -A INPUT -s 127.0.0.0/8 -j DROP
    sudo iptables -A OUTPUT -p tcp -m state --state NEW,ESTABLISHED -j ACCEPT
    sudo iptables -A OUTPUT -p udp -m state --state NEW,ESTABLISHED -j ACCEPT
    sudo iptables -A OUTPUT -p icmp -m state --state NEW,ESTABLISHED -j ACCEPT
    sudo iptables -A INPUT -p tcp -m state --state ESTABLISHED -j ACCEPT
    sudo iptables -A INPUT -p udp -m state --state ESTABLISHED -j ACCEPT
    sudo iptables -A INPUT -p icmp -m state --state ESTABLISHED -j ACCEPT
    sudo iptables -A INPUT -p tcp --dport 22 -m state --state NEW -j ACCEPT
    sudo iptables-save > /etc/iptables/rules.v4

    # Install necessary packages for UFW
    install_package "ufw"

    # Enable and start UFW service
    enable_and_start_service "ufw"

    # Configure UFW
    configure_ufw_loopback
    configure_ufw_outbound
    configure_ufw_open_ports
    set_ufw_default_deny

    # Enable UFW
    sudo ufw enable
}

# Run the main function
perform_security_configurations

echo "Security configurations applied successfully!"
