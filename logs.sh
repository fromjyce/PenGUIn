#!/bin/bash
if ! command -v journalctl &> /dev/null; then
    echo "Error: journalctl command not found. This script requires systemd."
    exit 1
fi


log_options="--pager-end"
if [ "$EUID" -ne 0 ]; then
    log_options="$log_options --user"
fi

# Display system logs and redirect to a read-only file
journalctl $log_options > system_logs.txt

# Make the log file read-only
chmod 400 system_logs.txt
