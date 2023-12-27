#!/bin/bash

# Enable firewall
sudo ufw enable
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Update and upgrade packages
sudo apt update
sudo apt upgrade -y

# Install and configure fail2ban
sudo apt install -y fail2ban
sudo systemctl enable fail2ban
sudo systemctl start fail2ban

# Configure Fail2Ban to allow only 3 login attempts
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
sudo sed -i 's/maxretry = 5/maxretry = 3/' /etc/fail2ban/jail.local

# Disable unnecessary services
# Replace <service_name> with the appropriate service name you want to disable

services_to_disable=("telnet" "vsftpd" "cups" "bluetooth" "avahi-daemon" "bind9" "snmpd" "cups" "wpa_supplicant" "nmbd" "smbd" "mysql" "mysqld" "postgresql")

for service in "${services_to_disable[@]}"; do
    sudo systemctl disable "$service"
    sudo systemctl stop "$service"
done

# Set up automatic security updates
sudo apt install -y unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades

# Enable automatic security updates for packages
echo 'APT::Periodic::Update-Package-Lists "1";' | sudo tee -a /etc/apt/apt.conf.d/10periodic
echo 'APT::Periodic::Download-Upgradeable-Packages "1";' | sudo tee -a /etc/apt/apt.conf.d/10periodic
echo 'APT::Periodic::AutocleanInterval "7";' | sudo tee -a /etc/apt/apt.conf.d/10periodic
echo 'APT::Periodic::Unattended-Upgrade "1";' | sudo tee -a /etc/apt/apt.conf.d/10periodic

# Disable root login
sudo sed -i 's/PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config
sudo systemctl restart sshd
