#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <vpn_interface>"
    exit 1
fi

vpn_interface="$1"

# Check if the WireGuard VPN interface is currently active
if wg show "$vpn_interface" &>/dev/null; then
    # If active, turn off the VPN
    sudo wg-quick down "$vpn_interface"
    echo "WireGuard VPN turned off."
else
    # If not active, turn on the VPN
    sudo wg-quick up "$vpn_interface"
    echo "WireGuard VPN turned on."
fi
