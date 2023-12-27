#!/bin/bash
sudo apt update
updates_available=$(sudo apt list --upgradable 2>/dev/null | grep -c "\[upgradable\]")
if [ $updates_available -gt 0 ]; then
    
    sudo apt upgrade -y
    echo "Updates installed successfully."
else
    echo "No updates available."
fi
