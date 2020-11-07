from spinup import ppo_pytorch as ppo
import torch
import torch.nn as nn
import gym
import cartpole_swingup_envs

env_fn=lambda:gym.make('CartPoleSwingUpContinuous-v0')
ac_kwargs=dict(hidden_sizes=[64,64],activation=nn.ReLU)
logger_kwargs=dict(output_dir='output',exp_name='cartpole_swingup')
ppo(env_fn=env_fn,ac_kwargs=ac_kwargs,steps_per_epoch=5000,
    epochs=300,logger_kwargs=logger_kwargs)