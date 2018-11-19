## Give everyone their own directory
# for CG in {00..15}; do
	# if ! [ -d CG$CG ]; then
		# mkdir CG$CG
		# mv *_$CG.* CG$CG
		# cp $KLUSTERING/tetrode.prb CG$CG 
	# fi
# done
from pathlib import Path
import shutil

root = Path(".").resolve()
template_prb = Path(__file__).resolve().parent / 'tetrode.prb'

for CG in range(16):
	dir_name = 'CG{group:02d}'.format(group=CG)
	new_dir = root / dir_name
	
	print('############## {} #############'.format(CG))
	# Create new directories if needed
	if not new_dir.exists():
		print('Creating {}'.format(new_dir))
		new_dir.mkdir()
	else:
		print('Skipping {}'.format(new_dir))
		
	# Move .dat and .prm and .prb files into new directories
	files = root.glob('*_{:02d}.*'.format(CG))
	for f in files:
		shutil.move(str(f), str(new_dir))
	
	# Copy the tetrode.prb file
	shutil.copy(str(template_prb), str(new_dir))

