# Building 

## Requirement 

Keystone documentation recommand using Ubuntu 16.04/18.04/20.04 and derivative. This artifact has been tested using Ubuntu 20.04.6.

The following dependencies are required to build the systems using buildroot

```bash
sudo apt update
sudo apt install autoconf automake autotools-dev bc \
bison build-essential curl expat jq libexpat1-dev flex gawk gcc git \
gperf libgmp-dev libmpc-dev libmpfr-dev libtool texinfo tmux \
patchutils zlib1g-dev wget bzip2 patch vim-common lbzip2 python3 \
pkg-config libglib2.0-dev libpixman-1-dev libssl-dev screen \
device-tree-compiler expect makeself unzip cpio rsync cmake ninja-build p7zip-full libncurses-dev
```

## Platform and variant selection

While Keystone originally support both QEMU and HiFive Unmatched Rev. B platform, this work currently only support HiFiuve Unmatched Rev. B.


> This is due to the version bump of buildroot/Linux kernel which introduced a few incompatibilities in the builds. We fixed thoses necessary for HiFive Unmatched but were not able to totally fix QEMU and while the build process succed, there is currently still a crash at boot.

The platform is selected using the `KEYSTONE_PLATFORM` variable. When running from this root directory, it is set to `KEYSTONE_PLATFORM=hifive_unmatched` by default.

The system variant use the `RT=y/n` flag (`RT=n` by default) to know whether to build the stock version (without the PREEMPT\_RT patches) of the real-time one.

## Build

Current configuration correspond to the system used for the article. If you want to modified them before building the systems, see [## Configurations](##Configurations).

Set the `RT=y/n` depending on which variant you want to build.

```bash
make RT=y
```

The sdcard.img will be located in the `keystone-rt/(...)/buildroot.build/images/sdcard.img`

First build will that a lot of time because buildroot has to download and build all the toolchain/kernel/subsystel/package. These are being re-used for later build.

## Configurations

The buildroot configuration can be edited using the following commands (change or remove the `RT` flag if necessary)

```bash
make RT=y buildroot-configure
```

The actual configs are located in [overlays/keystone/configs](keystone-rt/overlays/keystone/configs) under `riscv64_hifive_unmatched_defconfig` and `riscv64_hifive_unmatched_rt_defconfig`.

The corresponding Linux configuration can be edited with

```bash
make RT=y linux-configure
```

The linux config are located in [overlays/keystone/board/sifive/hifive-unmatched](keystone-rt/overlays/keystone/board/sifive/hifive-unmatched) under `linux-sifive-unmatched-defconfig` and `linux-sifive-unmatched-rt-defconfig`.

Depending on what you have change, the target may need a global rebuild or not. See the [Buildroot manual](https://docs.keystone-enclave.org/en/latest/Getting-Started/QEMU-Compile-Sources.html) for more explaination.

## Advanced buildroot commands

To acces all buildroot commands, you need to change the cwd to `cd keystone-rt` (or directly call the [keystone-rt/Makefile](keystone-rt/Makefile) using `make -C keystone-rt`). Here you need to manually set `KEYSTONE_PLATFORM=hifive_unmatched` then you can use the `BUILDROOT_TARGET=...`to call specific buildroot commands.

For more information on the available commands and arguments, see the [keystone documentation](https://docs.keystone-enclave.org/en/latest/Getting-Started/QEMU-Compile-Sources.html) and [Buildroot manual](https://docs.keystone-enclave.org/en/latest/Getting-Started/QEMU-Compile-Sources.html)
