# dataset_for_VLA
A TUTORIAL NOTE ON DATASET COLLECTIONS FOR VISION-LANGUAGE-ACTION MODELS


## Demo

<div align="center">
  <img src="images/ravens_tasks.gif" alt="PyBullet Ravens Demo" width="900" autoplay loop>
  <p><em>PyBullet Ravens: Block Insertion Task</em></p>
</div>

## Quick Start

###Ravens Install Dependencies
```bash
# Clone Ravens framework
git clone https://github.com/trustmlyoungscientist/dataset_for_VLA.git
cd dataset_for_VLA/ravens

conda create --name ravens python=3.7 -y
conda activate ravens
sudo apt-get update
sudo apt-get -y install gcc libgl1-mesa-dev
pip install -r requirements.txt
python setup.py install --user

# Collect demonstration data
python ravens/demos.py --assets_root=./ravens/environments/assets/ --task=block-insertion --mode=train --n=100 --disp=True

# Other tasks
python ravens/demos.py --task=place-red-in-green --mode=train --n=50
python ravens/demos.py --task=towers-of-hanoi --mode=train --n=50


###Libero Install Dependencies
```bash
cd dataset_for_VLA
conda create -n libero python=3.8.13
conda activate libero
git clone https://github.com/Lifelong-Robot-Learning/LIBERO.git
cd LIBERO
pip install -r requirements.txt
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113
mv libero-master images/libero-master 
