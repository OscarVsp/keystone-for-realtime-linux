#!/bin/bash

# Initialize variables
RT=0
SD_DEV=mmcblk0

# Parse command-line arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        --rt)
            RT=1
            shift 1
            ;;
        *)
            echo "Unknown option: $1"
            echo "Usage: $0 [-rt]"
            echo "  --rt             Select RT source"
            exit 1
            ;;
    esac
done

if [ "$RT" -eq 1 ]; then
    TYPE="_rt"
else
    TYPE=""
fi;



if lsblk | grep -q "$SD_DEV"; then
    echo "flashing device $SD_DEV with file keystone-rt/build-hifive_unmatched64$TYPE/buildroot.build/images/sdcard.img"
    sudo dd if=keystone-rt/build-hifive_unmatched64$TYPE/buildroot.build/images/sdcard.img of=/dev/$SD_DEV bs=1M status=progress
else
    echo "Device $SD_DEV is not connected."
fi
