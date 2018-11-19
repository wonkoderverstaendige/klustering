# imports
from pprint import pprint
from matplotlib import pyplot as plt
from pprint import pformat
from collections import OrderedDict
import argparse
from pathlib import Path


# function definitions
def read_probe(prb_path):
    with open(prb_path) as prb_file:
        content = prb_file.read()
    probe = OrderedDict()
    exec(content, {}, probe)
    return probe

    
def scale_probe(probe, scale_factor=5):
    channel_groups = probe['channel_groups']
    for group_id, group in channel_groups.items():
        geometry = group['geometry']

        # Position offset for this group based on its id
        dx = group_id % 4 * scale_factor
        dy = -(group_id // 4 * scale_factor)  # beware integer divisions/modulus with negative numbers!

        # Iterate over the channels and their x- and y- coordinates
        for channel_id, channel_pos in geometry.items():

            # calculate new position
            new_pos = (channel_pos[0] + dx, channel_pos[1] + dy)

            # Update dictionary
            geometry[channel_id] = new_pos
    return channel_groups

    
def write_probe(probe, prb_path, radius=None):

    # test stuff
    if not 'radius' in probe:
        pass
    
    if not 'total_nb_channels' in probe:
        pass
    
    with open(str(prb_path), 'w') as new_prb:
        for variable_name, variable_value in probe.items():
            if variable_name == 'radius' and radius is not None:
                variable_value = radius

            new_prb.write('{variable_name} = {variable_value}\n'.format(variable_name=variable_name,
                                                                       variable_value=pformat(variable_value, indent=2)))

                                                                       
def plot_probe(probe):
    channel_groups = probe['channel_groups']
    # color individual channels
    colors = 'rgby'
    
    # Create plot and set x- and y- limits to not cut off the outer groups
    fig, ax = plt.subplots(figsize=(10, 10))
#     ax.set_xlim((scale_factor * -.3, scale_factor * 3.5))
#     ax.set_ylim((scale_factor * -3.5, scale_factor * .5))

    # Iterate over the channel groups
    for group_id, group in channel_groups.items():
        geometry = group['geometry']

        # Iterate over the channels and their x- and y- coordinates
        first_channel = True
        for channel_id, channel_pos in geometry.items():
            if first_channel:
                ax.annotate("Group {}".format(group_id), xy=(channel_pos[0], channel_pos[1]))
                first_channel = False

            # plot new positions
            ax.plot(channel_pos[0], channel_pos[1], colors[channel_id%4] + 'o')

                                                                                                                                                                                                                                                                                                
# if __name__ == '__main__':


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='Path to probe from data man')
    parser.add_argument('output_path', help='Probe file output path.')
    parser.add_argument('-f', '--force', action='store_true', help='Overwrite existing files')
    
# parse cli arguments
    cli_args = parser.parse_args()
    prb_path = Path(cli_args.path).resolve()
    if not prb_path.exists():
        raise FileNotFoundError('No such file: {}'.format(prb_path))
    
    new_prb_path = Path(cli_args.output_path).resolve()
    if new_prb_path.exists() and not cli_args.force:
        raise IOError('File exists!')

    scale_factor = 100
    radius = scale_factor * 0.4
    # read probe
    probe = read_probe(prb_path)

    # modify probe
    scale_probe(probe, scale_factor=scale_factor)

    # write it out
    write_probe(probe, new_prb_path, radius=radius)

    # optionally, plot it
    #plot_probe(probe)