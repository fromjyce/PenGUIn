#!/usr/bin/env bash

# Function to perform USB storage audit
perform_usb_audit() {
    l_output=""
    l_output2=""
    l_mname="usb-storage" # set module name

    # Check how module will be loaded
    l_loadable="$(modprobe -n -v "$l_mname")"
    if grep -Pq -- '^\h*install \/bin\/(true|false)' <<< "$l_loadable"; then
        l_output="$l_output\n - module: \"$l_mname\" is not loadable: \"$l_loadable\""
    else
        l_output2="$l_output2\n - module: \"$l_mname\" is loadable: \"$l_loadable\""
    fi

    # Check if the module is currently loaded
    if ! lsmod | grep "$l_mname" > /dev/null 2>&1; then
        l_output="$l_output\n - module: \"$l_mname\" is not loaded"
    else
        l_output2="$l_output2\n - module: \"$l_mname\" is loaded"
    fi

    # Check if the module is deny-listed
    if grep -Pq -- "^\h*blacklist\h+$l_mname\b" /etc/modprobe.d/*; then
        l_output="$l_output\n - module: \"$l_mname\" is deny-listed in: \"$(grep -Pl -- "^\h*blacklist\h+$l_mname\b" /etc/modprobe.d/*)\""
    else
        l_output2="$l_output2\n - module: \"$l_mname\" is not deny-listed"
    fi

    # Report results. If no failures output in l_output2, we pass
    if [ -z "$l_output2" ]; then
        echo -e "\n- Audit Result:\n ** PASS **\n$l_output\n"
    else
        echo -e "\n- Audit Result:\n ** FAIL **\n - Reason(s) for audit failure:\n$l_output2\n"
        [ -n "$l_output" ] && echo -e "\n- Correctly set:\n$l_output\n"
    fi
}

# Function to perform USB storage remediation
perform_usb_remediation() {
    l_mname="usb-storage" # set module name

    # Set module to be not loadable
    if ! modprobe -n -v "$l_mname" | grep -P -- '^\h*install \/bin\/(true|false)'; then
        echo -e " - Setting module: \"$l_mname\" to be not loadable"
        echo -e "install $l_mname /bin/false" >> /etc/modprobe.d/"$l_mname".conf
    fi

    # Unload the module if currently loaded
    if lsmod | grep "$l_mname" > /dev/null 2>&1; then
        echo -e " - Unloading module \"$l_mname\""
        modprobe -r "$l_mname"
    fi

    # Deny-list the module
    if ! grep -Pq -- "^\h*blacklist\h+$l_mname\b" /etc/modprobe.d/*; then
        echo -e " - Deny-listing \"$l_mname\""
        echo -e "blacklist $l_mname" >> /etc/modprobe.d/"$l_mname".conf
    fi
}

# Block USB ports
block_usb_ports() {
    echo 'ACTION=="add", SUBSYSTEM=="usb", TEST=="authorized_default", ATTR{authorized_default}="0"' | sudo tee /etc/udev/rules.d/00-usb-autorules.rules

    # Reload udev rules
    sudo udevadm control --reload-rules
    sudo udevadm trigger
}
perform_usb_audit
perform_usb_remediation
block_usb_ports
