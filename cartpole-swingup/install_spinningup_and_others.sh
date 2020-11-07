sudo apt update && sudp apt install -y libopenmpi-dev
sudo apt install -y git

# Spinningup needs python 3.6
git clone https://github.com/mahyaret/spinningup.git
cd spinningup
pip install -e .

pip install matplotlib
pip install numpy
pip install opencv-python
pip install pybullet
pip install tensorboardX

git clone https://github.com/jfpettit/cartpole-swingup-envs.git
pip install -e cartpole-swingup-envs