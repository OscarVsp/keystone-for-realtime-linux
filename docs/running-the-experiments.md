# Running the experiments

## Experiment 1

This experiment measure the startup scheduling latencies of high-priority Linux process during high load. Cyclictest is used to measure the latencies while iperf3 and stress-ng put pressurs on the system.

The following command can be used to run this experiment:

```bash
./run-linux-cyclictest.sh --duration 10m
```

> Since the stressors will try to use all ressources available, the system wil likely become unresponsice

The latencies are recorded in the `cyclictest.log` file.

## Experiment 2

This experiment is basically the same as the previous one, but with the introduction of Keystone enclave in the background.

The following command can be used to run this experiment:

```bash
./run-linux-cyclictest.sh --duration 10m --enclave-loop
```

The latencies are recorded in the `cyclictest.log` file.

### Experiment 3

This experiment measure the startup scheduling latencies of keystone enclave spawn from high priority process. A modified version of cyclictest is used insided an enclave to measure the latencies while iperf3 and stress-ng put pressurs on the system.

The following command can be used to run this experiment:

```bash
./run-enclave-cyclictest.sh --duration 10m --threads 2 --loops 60 --delay 10 --cpus 0-1
```

> Due to an issue from Keystone, creating more than ~150 enclaves from a process will likely result in core halt. To get more measurement, you can simply save the `cyclictest.log` file then re-run the same cmd.

The latencies are recorded in the `cyclictest.log` file.
