# Making figures

All the figure are handle by the [results/generate-figures.py](results/generate-figures.py) python scripts.

## Requirements

We sugest to first create a virtual environnement then instaling the requirements as follow 

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r results/requirements.txt
```

## Data

The measurements made for the article are available in the [results/archive.tar.gz](results/archive.tar.gz) archive. The expected structure is the following:

```
.
└── results/
    ├── figures/
    ├── hifive_unmatched/
    ├── keystone-hybrid/
    ├── keystone-mixted/
    └── enclave-startup.log
```

The bottom section of the [results/generate-figures.py](results/generate-figures.py) file contains the configuration to load each measurement files and create the figures.

If you have generate you own data by running the experiment, either match the structure above or adapte the [results/generate-figures.py](results/generate-figures.py) script to point to you data.

## Usage

You can called the script directly from the root dir as following:

```bash
python3 results/generate-figures.py
```
The figures will be generated into [results/figures](results/figure)
