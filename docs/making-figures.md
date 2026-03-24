# Making figures

All the figures are handled by the [results/generate-figures.py](../results/generate-figures.py) Python scripts.

## Requirements

We suggest to first create a virtual environement (`sudo apt install python3-venv` if you don't have python-venv yet) then installing the requirements as follows:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r results/requirements.txt
```

## Data

The bottom section of the [results/generate-figures.py](../results/generate-figures.py) file contains the configuration to load each measurement file and create the figures.

You can either:

- Use the data from the article (provided in the [results/archive.tar.gz](../results/archive.tar.gz))
- Use the data you generated from your own experiment.

The structure expected by the script is the following:

```
.
└── results/
    ├── linux/
    │   ├── realtime/
    │   │   └── cyclictest.log
    │   └── stock/
    │       └── cyclictest.log
    ├── mixted/
    │   ├── realtime/
    │   │   └── cyclictest.log
    │   └── stock/
    │       └── cyclictest.log
    ├── real-time enclave/
    │   ├── 1 thread/
    │   │   ├── realtime/
    │   │   │   └── cyclictest.log
    │   │   └── stock/
    │   │       └── cyclictest.log
    │   └── 2 threads/
    │       ├── realtime/
    │       │   └── cyclictest.log
    │       └── stock/
    │           └── cyclictest.log
    └── enclave-startup.log
```

If you use the data provided, you can simply extract the archive using the following command, and the structure should be correct.

```bash
tar -xvzf results/archive.tar.gz -C results
```

If you have generated your own data by running the experiment, either match the structure above or adapt the [results/generate-figures.py](../results/generate-figures.py) script to point to your data.

## Usage

Make sure you are using the virtual environnement:

```bash
source .venv/bin/activate
```

You can call the script directly from the root directory as follows:

```bash
python3 results/generate-figures.py
```

The figures will be generated into `results/figures`.

You can easily visualized them all on [results/figures/fig.md](../results/figures/fig.md).
