#!/bin/bash

set -e

# Initialize variables
RT=0
SD_DEV="sda"
MUX_DEV="/dev/sg0"
IP="lab-pi.local"
ON=0
SKIP_TRANSFER=0

# Parse command-line arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        --rt)
            RT=1
            shift 1
            ;;
        -a)
            if [[ -n "$2" ]]; then
                IP="$2"
                shift 2
            else
                echo "Error: -a requires an IP address"
                exit 1
            fi
            ;;
        --on)
            ON=1
            shift 1
            ;;
        --skip-transfer)
            SKIP_TRANSFER=1
            shift 1
            ;;
        *)
            echo "Usage: $0 -a IP [--rt] [--on] [--skip-transfer]"
            echo "  -a IP           Remote IP address (required)"
            echo "  --rt            Select RT source"
            echo "  --on            Power on the device after flashing"
            echo "  --skip-transfer Skip file transfer (assume file is already on remote host)"
            exit 1
            ;;
    esac
done

# Check if IP is provided
if [ -z "$IP" ]; then
    echo "Error: -a IP is required"
    exit 1
fi

if [ "$RT" -eq 1 ]; then
    TYPE="_rt"
else
    TYPE=""
fi;

if [ "$SKIP_TRANSFER" -eq 0 ]; then
    echo "Sending sdcard.img for type realtime=$RT to remote $IP"
    if ! scp -o StrictHostKeyChecking=no keystone-rt/build-hifive_unmatched64$TYPE/buildroot.build/images/sdcard.img pi@$IP:~/; then
        echo "Error: Failed to send sdcard.img to remote host"
        exit 1
    fi
else
    echo "Skipping file transfer (--skip-transfer specified)"
fi

echo "Connecting to remote device and sending usbsdmux command"
ssh -o StrictHostKeyChecking=no pi@$IP <<EOF
echo "switching mux to host"
usbsdmux $MUX_DEV host

# Check if mux is properly switched to host
if ! usbsdmux $MUX_DEV get | grep -q "host"; then
    echo "Error: Failed to switch mux to host mode"
    exit 1
fi

if lsblk | grep -q "$SD_DEV"; then
    echo "flashing device $SD_DEV"
    sudo dd if=~/sdcard.img of=/dev/$SD_DEV bs=1M status=progress
else
    echo "Device $SD_DEV is not connected."
    exit 1
fi
usbsdmux $MUX_DEV dut
EOF

if [ "$ON" -eq 1 ]; then
    echo "Powering on the device"
    if ! ssh -q -o StrictHostKeyChecking=no pi@$IP <<EOF
usbsdmux $MUX_DEV gpio 0 0
sleep 1
usbsdmux $MUX_DEV gpio 0 1
EOF
    then
        echo "Error: Failed to power on the device"
        exit 1
    fi
fi