# Spike sorting pipeline


## For manual clustering on your computer

- Download and install miniconda or Anaconda Python
- During installation you will be asked whether you want Anaconda to be added to the Path. Do so.

- Download and install the Visual Studio C++ Build Tools
	- `http://landinghub.visualstudio.com/visual-cpp-build-tools`, grab the 2015 one and install

- Download and install git (unix people will know, else: [Github for Windows](https://git-for-windows.github.io/))

- Download the `binarymasksklusta.yml` from `\\tompouce\shared\TetrodeSpikeSortingPipeline\`

- Open the windows terminal (Arto: `Windows+R`, type `cmd`, hit `Enter`)

- `cd` into the directory with the binarymasks.yml

- Run `conda env create -n klusta_bm -f binarymasksklusta.yml`

- Each time you want to use it, you need to activate the environment with `activate klusta_bm`

- Change with `cd` into the directory with your result files

- Run `phy kwik-gui [the path to the .kwik file]`, for example `phy kwik-gui result.kwik`



## For running the clustering on a machine

- Download the source code to dataman and ophys_io (rename folder to oio)

- `pip install -e oio dataman`

- Shell script at `/tompouce/homes/reichler/code/Klustering/kluster`



## Pre-processing

- Create a probe (.prb) file with channel layout
	- Refer to e.g. `\\tompouce\homes\reichler\data\m26484\m26484_16.prb`

- Create a flat binary file (.dat).
	- dm conv [files] -l [.prb file] -D [duration]`

- After or during conversion, rearrange channels to match tetrode order

- Re-reference
	- `dm ref [.dat file]`

- Other pre-processing steps (e.g. artifact removal)
	- `...`

- Split into tetrodes (4 channels each)
	- `dm split -l [.prb file] OR by grouping`

- Generate parameter (.prm) files



## Automatic detection and sorting

Klusta will first run spikedetekt, then klustakwik2. Spikedetekt estimates the thresholds for spike detection, detects threshold crossings and calculates the features for the detected spikes. Klustakwik2 clusters the spikes.


- Run `klusta` on .prm file

	- Note: Keep each run in its own sub folder or they may interfere

- Delete .spikedetekt and .klustakwik2 temprorary folders, they slow down copying a lot

- Keep the .dat, .kwik, .kwx, .prm, .prb, .log files



## Manual curation


- Run `phy kwik-gui` on .kwik file



## Analyze spikes


- .kwik file is hdf5 file containing information about the found spikes in the clusters


## Notes:
- install visual studio redist


