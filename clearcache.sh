#!/bin/bash

sudo apt clean


if command -v dnf &> /dev/null; then
    sudo dnf clean all
elif command -v yum &> /dev/null; then
    sudo yum clean all
fi


sudo journalctl --vacuum-size=50M

# Clear Firefox Browser Cache
# Replace 'your_user' with your actual username
rm -r /home/your_user/.cache/mozilla/firefox/*.default/cache2/

# Clear Chrome/Chromium Browser Cache
# Replace 'your_user' with your actual username
rm -r /home/your_user/.cache/google-chrome/Default/Cache/

echo "Cache clearing completed for better performance (excluding temporary files)."
