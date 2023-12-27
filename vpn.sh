#!/bin/bash

openvpn_status() {
    if command -v openvpn &> /dev/null; then
        sudo openvpn --status /var/run/openvpn/server.status
    else
        echo "OpenVPN is not installed."
    fi
}


wireguard_status() {
    if command -v wg &> /dev/null; then
        sudo wg show
    else
        echo "WireGuard is not installed."
    fi
}


strongswan_status() {
    if command -v ipsec &> /dev/null; then
        sudo ipsec status
    else
        echo "StrongSwan is not installed."
    fi
}


main() {
    echo "Checking VPN statuses..."

    echo -e "\nOpenVPN Status:"
    openvpn_status

    echo -e "\nWireGuard Status:"
    wireguard_status

    echo -e "\nStrongSwan Status:"
    strongswan_status
}

# Run the main function
main
