# ETL Workflows 2

This directory contains a simple ETL pipeline implementation.

- `pipeline.ipynb` - the notebook used to write the pipeline step by step.
- `pipeline.py` - the first Python file that contains the entire pipeline in one script.
- `extract.py` - the modularized extraction logic extracted from `pipeline.py`.
- `load.py` - the modularized loading logic extracted from `pipeline.py`.
- `transform.py` - the modularized transformation logic extracted from `pipeline.py`.
- `main.py` - the modularized entry point that ties the extract, transform, and load modules together.
