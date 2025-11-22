#!/bin/bash
#
#The script installs Nginx on the system while writing structured log entries for each step of the process.

#Log file location.
log_file="$(dirname "$0")/../logs/nginx_script.log"
script_name="$(basename "$0")"

#logging format.
log() {
    printf "%s - %s - %s - %s\n" \
        "$(date '+%Y-%m-%d %H:%M:%S,%3N')" \
        "$1" \
        "$script_name" \
        "$2" >> "$log_file"
}

#Script start.
log INFO "Starting Bash script..."

#Check if nginx is already installed.
if dpkg -s nginx >/dev/null 2>&1; then
    log INFO "Nginx already installed."
    exit 0
fi

#Install nginx.
log INFO "Installing Nginx..."
sudo apt update -y >/dev/null 2>&1
sudo apt install -y nginx >/dev/null 2>&1

#Check installation result.
if [ $? -eq 0 ]; then
    log INFO "Nginx installed successfully."
else
    log ERROR "Nginx installation failed"
    exit 1
fi

log INFO "Bash script executed successfully."