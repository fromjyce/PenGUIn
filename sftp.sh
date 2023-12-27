#!/bin/bash

is_package_installed() {
    dpkg-query -s "$1" &>/dev/null
}


install_package() {
    if ! is_package_installed "$1"; then
        echo "Installing $1..."
        sudo apt-get install -y "$1"
    fi
}


remove_package() {
    if is_package_installed "$1"; then
        echo "Removing $1..."
        sudo apt-get purge -y "$1"
    fi
}


remove_package "vsftpd"
install_package "openssh-server"
echo "SFTP hardening script executed successfully!"
