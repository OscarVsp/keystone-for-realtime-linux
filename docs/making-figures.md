# Making figures

All the figure are handle by the [results/generate-figures.py](results/generate-figures.py) python scripts.

## Requirements

We sugest to first create a virtual environnement then instaling the requirements are follow 

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r results/requirements
```

## Configuration

The bottom section of the file contains the configuration to load each measurement file and to create the graph. The current configuration correspond to the one used for the article. You can comment out the part you do not want/need.

## Usage

You can called the script directly from the root dir as following:

```bash
python results/generate-figures.py
```

The figures will be generated into [results/figures](results/figure)

