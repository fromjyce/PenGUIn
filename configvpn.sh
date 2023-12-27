#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <wireguard_config_file>"
    exit 1
fi

wireguard_config_file="$1"


if [ ! -f "$wireguard_config_file" ]; then
    echo "Error: File not found - $wireguard_config_file"
    exit 1
fi

# Open the contents for editing using nano (you can use any text editor of your choice)
nano "$wireguard_config_file"
