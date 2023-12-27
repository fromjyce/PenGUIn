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

# Function to create and populate an ipset with Tor exit nodes
configure_tor_ipset() {
    ipset create tor iphash

    curl -sSL "https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=$(curl icanhazip.com)" | sed '/^#/d' | while read IP; do
        ipset -q -A tor $IP
    done
}

# Function to block ipset with iptables
block_tor_ipset_with_iptables() {
    sudo iptables -A INPUT -m set --match-set tor src -j DROP
}

# Main function to perform Tor IPset configuration
configure_tor_ipset_and_iptables() {
    install_package "ipset"

    configure_tor_ipset
    block_tor_ipset_with_iptables
}

# Run the main function
configure_tor_ipset_and_iptables

echo "Tor IPset configuration applied successfully!"
