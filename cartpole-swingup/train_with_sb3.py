import gym
from stable_baselines3 import A2C,PPO
import cartpole_swingup_envs

env=gym.make('CartPoleSwingUpContinuous-v0')
model=PPO('MlpPolicy',env,verbose=1)
model.learn(total_timesteps=1000000)

obs=env.reset()
for i in range(9000):
    action,_state=model.predict(obs,deterministic=True)
    obs,reward,done,info=env.step(action)
    env.render()
    if done:
        obs=env.reset()
