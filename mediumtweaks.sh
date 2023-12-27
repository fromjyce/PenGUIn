#!/bin/bash

# Enable firewall
sudo ufw enable
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Allow necessary services
sudo ufw allow ssh
sudo ufw allow 80  # Allow HTTP traffic
sudo ufw allow 443  # Allow HTTPS traffic

# Block unnecessary ports
sudo ufw deny 23  # Block Telnet
sudo ufw deny 21  # Block FTP
# Add more lines to block other unnecessary ports as needed

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
services_to_disable=(
    "telnet" "vsftpd" "cups" "bluetooth" "avahi-daemon"
    "bind9" "snmpd" "cups" "wpa_supplicant" "nmbd"
    "smbd" "mysql" "mysqld" "postgresql" "rpcbind"
    "nfs-common" "nfs-kernel-server" "apache2" "nginx"
)

for service in "${services_to_disable[@]}"; do
    sudo systemctl stop "$service"
    sudo systemctl disable "$service"
done

# Set up automatic security updates
sudo apt install -y unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades

# Enable automatic security updates for packages
echo 'APT::Periodic::Update-Package-Lists "1";' | sudo tee -a /etc/apt/apt.conf.d/10periodic
echo 'APT::Periodic::Download-Upgradeable-Packages "1";' | sudo tee -a /etc/apt/apt.conf.d/10periodic
echo 'APT::Periodic::AutocleanInterval "7";' | sudo tee -a /etc/apt/apt.conf.d/10periodic
echo 'APT::Periodic::Unattended-Upgrade "1";' | sudo tee -a /etc/apt/apt.conf.d/10periodic

# Disable root login and permit only key-based authentication
sudo sed -i 's/PermitRootLogin yes/PermitRootLogin without-password/' /etc/ssh/sshd_config

# Disable password authentication for SSH
sudo sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config

# Restart SSH service
sudo systemctl restart ssh

# Optionally, you can add more security configurations based on your requirements
