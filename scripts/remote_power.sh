#!/bin/bash

# Initialize variables
IP="lab-pi.local"
FORCE=0
ON=0
OFF=0
RESTART=0

# Parse command-line arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        -a)
            if [[ -n "$2" ]]; then
                IP="$2"
                shift 2
            else
                echo "Error: -a requires an IP address"
                exit 1
            fi
            ;;
        -f)
            FORCE=1
            shift 1
            ;;
        --on)
            ON=1
            shift 1
            ;;
        --off)
            OFF=1
            shift 1
            ;;
        --restart)
            RESTART=1
            shift 1
            ;;
        *)
            echo "Unknown option: $1"
            echo "Usage: $0 -a IP [--on|--off|--restart [-f]]"
            echo "  -a IP           Remote IP address (required)"
            echo "  --on            Power on the device"
            echo "  --off           Power off the device"
            echo "  --restart       Restart the device"
            echo "  -f              Force restart (use with --restart)"
            exit 1
            ;;
    esac
done

# Check if IP is provided
if [ -z "$IP" ]; then
    echo "Error: -a IP is required"
    exit 1
fi

if [ "$ON" -eq 1 ]; then

    if [ "$FORCE" -eq 1 ]; then
        echo "Sending forced power on command"
        ssh -q -o StrictHostKeyChecking=no pi@$IP <<EOF > /dev/null 2>&1
usbsdmux /dev/sg0 gpio 0 0
sleep 5
usbsdmux /dev/sg0 gpio 0 1
sleep 3
usbsdmux /dev/sg0 gpio 0 0
sleep 1
usbsdmux /dev/sg0 gpio 0 1
EOF
    else

        echo "Sending power on command"
        ssh -q -o StrictHostKeyChecking=no pi@$IP <<EOF > /dev/null 2>&1
usbsdmux /dev/sg0 gpio 0 0
sleep 1
usbsdmux /dev/sg0 gpio 0 1
EOF
    fi

elif [ "$OFF" -eq 1 ]; then

    if [ "$FORCE" -eq 1 ]; then
        echo "Sending forced power off command"
        ssh -q -o StrictHostKeyChecking=no pi@$IP <<EOF > /dev/null 2>&1
usbsdmux /dev/sg0 gpio 0 0
sleep 5
usbsdmux /dev/sg0 gpio 0 1
EOF
    else

        echo "Sending power off command"
        ssh -q -o StrictHostKeyChecking=no pi@$IP <<EOF > /dev/null 2>&1
usbsdmux /dev/sg0 gpio 0 0
sleep 1
usbsdmux /dev/sg0 gpio 0 1
EOF
    fi

elif [ "$RESTART" -eq 1 ]; then

    if [ "$FORCE" -eq 1 ]; then
        echo "Sending forced restart command"
        ssh -q -o StrictHostKeyChecking=no pi@$IP <<EOF > /dev/null 2>&1
usbsdmux /dev/sg0 gpio 0 0
sleep 5
usbsdmux /dev/sg0 gpio 0 1
sleep 3
usbsdmux /dev/sg0 gpio 0 0
sleep 1
usbsdmux /dev/sg0 gpio 0 1
EOF
    else
        echo "Sending restart command"
        ssh -q -o StrictHostKeyChecking=no pi@$IP <<EOF > /dev/null 2>&1
usbsdmux /dev/sg0 gpio 1 0
sleep 1
usbsdmux /dev/sg0 gpio 1 1
EOF
    fi

else
    echo "Error: must specify --on, --off, or --restart"
    exit 1
fi



