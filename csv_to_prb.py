#!/usr/bin/env python3

import csv
import argparse
from pathlib import Path
from itertools import combinations
from pprint import pformat as pretty


# geometries = {0: (1.25, 0.25),
              # 1: (1.25, -0.25),
              # 2: (0.75, 0.25),
              # 3: (0.75, -0.25)}
              
              
 
geometries = {0: (0, 0),
              1: (0, 1),
              2: (0, 2),
              3: (0, 3)}



def csv_to_prb(csv_path, prb_path):
    # read the file
    with open(csv_path.name) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        rows = list(reader)

    ids = [int(row[0]) - 1 for row in rows]
    descs = [row[1].strip() for row in rows]
    dead = sorted([ids[n] for n in range(len(ids)) if descs[n] not in ['tetrode']])

    for cg in range(len(ids)//4):
        print('Group {}:'.format(cg), ids[cg*4:(cg+1)*4])
    print(len(dead), 'dead channels:', dead)

    # Build channel group dictionaries
    groups = {}
    for cg in range(len(ids)//4):
        channels = ids[cg*4:(cg+1)*4]
        graph = list(combinations(channels, r=2))
        geometry = {ch: geometries[n] for n, ch in enumerate(channels)}
        description = {ch: desc for ch, desc in list(zip(ids, descs))[cg*4:(cg+1)*4]}
        groups[cg] = {'channels': channels,
                      'graph': graph,
                      'geometry': geometry,
                      'description': description}

    # Write fields out to prb file
    with open(prb_path.name, 'w') as prb:
        prb.write('# Dead channels contain all non-tetrode channels!\n\n')
        prb.write('dead_channels = {}\n'.format(pretty(dead)))
        prb.write('channel_groups = {}'.format(pretty(groups)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='Path to channel list in format "channel_num, description", e.g. "2, tetrode"')
    parser.add_argument('-o', '--prb_path', help='Probe file output path. Default is same as input, but with .prb suffix.')
    
    cli_args = parser.parse_args()
    csv_path = Path(cli_args.path).resolve()
    prb_path = cli_args.prb_path if cli_args.prb_path else csv_path.with_suffix('.prb')

    csv_to_prb(csv_path, prb_path)
