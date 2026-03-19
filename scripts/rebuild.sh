#!/bin/bash

# Fail fast, treat unset vars as errors, and make pipelines fail on first failing command
set -euo pipefail

# Enable command tracing only when VERBOSE=1
if [ "${VERBOSE:-0}" -ne 0 ]; then
    set -x
fi

# Print a helpful message on any error and exit
trap 'echo "ERROR: script failed at line $LINENO" >&2; exit 1' ERR

# Starting
echo "==> rebuild.sh starting"

# Initialize variables
_RT=0
_EX=0
_SM=0
_SD=0
_SKIP=0

# Parse command-line arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        --skip)
            _SKIP=1
            shift 1
            ;;
        --rt)
            _RT=1
            shift 1
            ;;
        --ex)
            _EX=1
            shift 1
            ;;
        --sm)
            _SM=1
            shift 1
            ;;
        --sd)
            _SD=1
            shift 1
            ;;
        *)
            echo "Unknown option: $1" >&2
            exit 1
            ;;
    esac
done

if [ "$_SD" -eq 1 ]; then
    sudo -v
fi;

export KEYSTONE_PLATFORM=hifive_unmatched
echo "Platform: $KEYSTONE_PLATFORM"

if [ "$_RT" -eq 1 ]; then
    export RT=y
fi;

echo "Options: RT=$_RT EX=$_EX SM=$_SM SD=$_SD SKIP=$_SKIP"

if [ "${VERBOSE:-0}" -ne 0 ]; then
    echo "Verbose tracing enabled (VERBOSE=1)"
fi

if [ "$_SKIP" -eq 0 ]; then

    if [ "$_EX" -eq 1 ]; then
        echo "==> Cleaning examples (keystone-examples-dirclean)"
        make -C keystone-rt BUILDROOT_TARGET=keystone-examples-dirclean
    fi;

    if [ "$_SM" -eq 1 ]; then
        echo "==> Cleaning sm (keystone-sm-dirclean)"
        make -C keystone-rt BUILDROOT_TARGET=keystone-sm-dirclean
    fi;

    echo "==> Building keystone-rt"
    make -C keystone-rt
fi;


if [ "$_SD" -eq 1 ]; then
    if [ "$_RT" -eq 1 ]; then
        echo "==> Flashing SD for RT"
        bash scripts/flash_sd.sh --rt
    else
        echo "==> Flashing SD"
        bash scripts/flash_sd.sh
    fi;
fi;

echo "==> rebuild.sh completed"
