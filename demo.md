

# Real-time attacks

## Core sharing

This demonstration shows that an enclave can not be garantee to run on a given interval. To give back control of the core to the host OS, the schedule is done on the host process (on the host OS). This mean that another enclave running can keep control of a core and therefore block the host OS (and therefore other enclave schedule) progression.

### Single-core

- Start qemu with one core.
```
cd ./keystone
make run QEMU_SMP=1
```

- Load the keystone driver
```
modprobe keystone-driver
```

- Start the `repeat-monitor` enclave
```
/usr/share/keystone/examples/repeat-monitor.ke
```

- On a second terminal (`./qemu_connect.sh`), start the `hold-cycle` enclave
```
/usr/share/keystone/examples/hold-cycle.ke
```

