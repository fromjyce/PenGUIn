#!/bin/bash


# Function to allow specific IP addresses or ranges
whitelist_ips() {
    # Add your custom whitelisted IP addresses or ranges here
    custom_whitelist=("192.168.1.1" "10.0.0.0/24")

    # Add commonly used friendly IP addresses
    friendly_whitelist=("8.8.8.8" "8.8.4.4" "1.1.1.1" "9.9.9.9")

    # Combine the custom and friendly whitelists
    whitelist=("${custom_whitelist[@]}" "${friendly_whitelist[@]}")

    # Allow traffic from whitelisted IPs
    for ip in "${whitelist[@]}"; do
        sudo iptables -A INPUT -s "$ip" -j ACCEPT
    done

    # Drop all other incoming traffic
    sudo iptables -A INPUT -j DROP
}
perform_whitelisting() {

    
    whitelist_ips
}

# Run the main function
perform_whitelisting

echo "Whitelisting configuration applied successfully!"
