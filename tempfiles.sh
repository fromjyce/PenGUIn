#!/bin/bash

# Clear system temporary directory
sudo rm -rf /tmp/*

# Clear user-specific temporary directories

rm -rf ~/.cache/*

rm -rf ~/.local/share/Trash/*

echo "Temporary file cleaning completed."
