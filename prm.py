#!/usr/bin/env python3
# Generate a .prm file for each .dat file in the working directory using the defaults from 
# tetrode.prm template file.
from pathlib import Path

defaults_path = Path(__file__).resolve().parent

paths = Path('.').glob('*_??.dat')

for p in paths:
    with open(p.with_suffix('.prm'), 'w') as prm, open(defaults_path / 'tetrode.prm', 'r') as template:
        for line in template:
            if 'experiment_name =' in line:
                line = "experiment_name = '{}'\n".format(str(p.with_suffix('')))
            prm.write(line)
