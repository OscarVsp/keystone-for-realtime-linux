# Making figures

All the figure are handle by the [results/generate-figures.py](../results/generate-figures.py) python scripts.

## Requirements

We sugest to first create a virtual environnement (`sudo apt install python3-venv` if you don't have python-venv yet) then instaling the requirements as follow 

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r results/requirements.txt
```

## Data

The bottom section of the [results/generate-figures.py](../results/generate-figures.py) file contains the configuration to load each measurement files and create the figures.

You can either:

- Use the data from the article (provided in the [results/archive.tar.gz](../results/archive.tar.gz))
- Use the data you generated from your own experiment

The expected structure is the following:

```
.
└── results/
    ├── figures/
    ├── hifive_unmatched/
    ├── keystone-hybrid/
    ├── keystone-mixted/
    └── enclave-startup.log
```

If you use the data provided, you can simply extract the archive using:

```bash
tar -xvzf results/archive.tar.gz -C results
```

If you have generate you own data by running the experiment, either match the structure above or adapte the [results/generate-figures.py](../results/generate-figures.py) script to point to you data.

## Usage

You can called the script directly from the root dir as following:

```bash
python3 results/generate-figures.py
```
The figures will be generated into `results/figures`
