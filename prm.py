#!/usr/bin/env python3
# Generate a .prm file for each .dat file in the working directory using the defaults from 
# tetrode.prm template file.
from pathlib import Path
import argparse

defaults_path = Path(__file__).resolve().parent / 'tetrode.prm'

parser = argparse.ArgumentParser()
parser.add_argument('-T', '--Template', help='Prm template path', default=defaults_path)

cli_args = parser.parse_args()

template_path = Path(cli_args.Template).resolve()
print(template_path)

#paths = Path('.').glob('*_?.dat')
paths = Path('.').glob('*_??.dat')

for p in paths:
    with open(str(p.with_suffix('.prm')), 'w') as prm, open(str(template_path), 'r') as template:
        for line in template:
            if 'experiment_name =' in line:
                line = "experiment_name = '{}'\n".format(str(p.with_suffix('')))
            prm.write(line)
