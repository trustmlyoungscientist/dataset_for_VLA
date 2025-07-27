# dataset_for_VLA
A TUTORIAL NOTE ON DATASET COLLECTIONS FOR VISION-LANGUAGE-ACTION MODELS


## Demo

<div align="center">
 <img src="images/ravens-tasks.gif" alt="PyBullet Ravens Demo" width="500">
 <p><em>PyBullet Ravens: Block Insertion Task</em></p>
</div>

## Quick Start

### Install Dependencies
```bash
conda create -n vla_dataset python=3.8
conda activate vla_dataset
pip install pybullet ravens-gym libero robosuite h5py numpy


# Clone Ravens framework
git clone https://github.com/google-research/ravens.git
cd ravens

# Collect demonstration data
python ravens/demos.py --assets_root=./ravens/environments/assets/ --task=block-insertion --mode=train --n=100 --disp=True

# Other tasks
python ravens/demos.py --task=place-red-in-green --mode=train --n=50
python ravens/demos.py --task=towers-of-hanoi --mode=train --n=50
