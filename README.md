# Keystone with Linux PREEMPT_RT: Real-Time Enclaves on RISC-V?

This is the artifact for our **Keystone with Linux PREEMPT_RT: Real-Time Enclaves on RISC-V?** paper submitted at the SysTEX"26 workshop.

This work aim at evaluating the impact of Keystone enclaves on a Linux system using the PREEMPT_RT patches. In particular, we focus on startup latencies of real-time tasks, both for mixted context (real-time task running along side Keystone enclave) and real-time enclave (Keystone enclave scheduled using real-time processes). The evaluation are done on a HiFive Unmatched Rev. B board.

This repo use a modified version of Keystone as a submodule. The main differences from the main keystone branch are:

- Updated Linux kernel version (from 6.1.32 to 6.6.87) to have acces to the PREEMPT_RT patches for RISC-V (available as standalone).
- New build target for RT variant which add the PREEMPT_RT patches and related Linux kernel configurations.

## Installation

Clone this repo then initialize the submodules:

```bash
git submodule update --init --recursive --depth 1
```

> There may be an error when trying to clone the `keystone-for-realtime-linux/keystone-rt/overlays/keystone/board/cva6/cva6-sdk/buildroot` submodule, which can be safely ignore as it is not used for this work

Keystone use Buildroot to build the systems. Since the build time can be quite significant (specially for fresh build), we provide ready to use image for the HiFive Unmatched board. This does method only require to have `git` and `dd` (or another tool to flash sd card).


If you want to build the image yourself to make some change, you will have some requirement for yourt system. Please refer to [docs/building.md.md](docs/building.md) in that case.



## Experiments

To run the same experiment as in our article, see [docs/running-the-experiments.md](docs/running-the-experiments.md)

## License


