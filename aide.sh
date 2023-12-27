#!/bin/bash


is_package_installed() {
    dpkg -l | grep -q "^ii\s*$1"
}


update_aide() {
    sudo apt update
    sudo apt install --only-upgrade aide
}


if ! is_package_installed aide; then
   
    sudo apt install aide aide-common
else
    
    update_aide
fi


sudo aideinit
sudo mv /var/lib/aide/aide.db.new /var/lib/aide/aide.db


sudo prelink -ua
sudo apt purge prelink


sudo grep -P -- '(\/sbin\/(audit|au)\H*\b)' /etc/aide/aide.conf || sudo bash -c 'cat <<EOL >> /etc/aide/aide.conf
# Audit Tools 
/sbin/auditctl p+i+n+u+g+s+b+acl+xattrs+sha512 
/sbin/auditd p+i+n+u+g+s+b+acl+xattrs+sha512 
/sbin/ausearch p+i+n+u+g+s+b+acl+xattrs+sha512 
/sbin/aureport p+i+n+u+g+s+b+acl+xattrs+sha512 
/sbin/autrace p+i+n+u+g+s+b+acl+xattrs+sha512 
/sbin/augenrules p+i+n+u+g+s+b+acl+xattrs+sha512
EOL'


sudo crontab -u root -l | grep -q '/usr/bin/aide.wrapper' || sudo bash -c 'echo "0 5 * * * /usr/bin/aide.wrapper --config /etc/aide/aide.conf --check" >> /etc/crontab'

sudo bash -c 'cat <<EOL > /etc/systemd/system/aidecheck.service
[Unit]
Description=Aide Check
[Service]
Type=simple
ExecStart=/usr/bin/aide.wrapper --config /etc/aide/aide.conf --check
[Install]
WantedBy=multi-user.target
EOL'

sudo bash -c 'cat <<EOL > /etc/systemd/system/aidecheck.timer
[Unit]
Description=Aide check every day at 5AM
[Timer]
OnCalendar=*-*-* 05:00:00
Unit=aidecheck.service
[Install]
WantedBy=multi-user.target
EOL'

sudo chown root:root /etc/systemd/system/aidecheck.*
sudo chmod 0644 /etc/systemd/system/aidecheck.*
sudo systemctl daemon-reload
sudo systemctl enable aidecheck.service
sudo systemctl --now enable aidecheck.timer


sudo /usr/bin/aide.wrapper --config /etc/aide/aide.conf --check

echo "AIDE installation, configuration, and scheduling complete. AIDE check executed."
