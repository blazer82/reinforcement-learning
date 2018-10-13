import gym
import numpy
from gym import error, spaces, utils
from gym.utils import seeding

class PyPokerEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.observation_space = spaces.Box(
            low=-1, high=1, shape=(32,), dtype=numpy.float32
        )

        self.action_space = spaces.Tuple((
            spaces.Discrete(3),
            spaces.Box(low=0, high=1, shape=(1,), dtype=numpy.float32)
            ))

    def step(self, action):
        """

        Parameters
        ----------
        action :

        Returns
        -------
        ob, reward, episode_over, info : tuple
            ob (object) :
                an environment-specific object representing your observation of
                the environment.
            reward (float) :
                amount of reward achieved by the previous action. The scale
                varies between environments, but the goal is always to increase
                your total reward.
            episode_over (bool) :
                whether it's time to reset the environment again. Most (but not
                all) tasks are divided up into well-defined episodes, and done
                being True indicates the episode has terminated. (For example,
                perhaps the pole tipped too far, or you lost your last life.)
            info (dict) :
                    diagnostic information useful for debugging. It can sometimes
                    be useful for learning (for example, it might contain the raw
                    probabilities behind the environment's last state change).
                    However, official evaluations of your agent are not allowed to
                    use this for learning.
        """
        
        return numpy.zeros((32,)), 0.0, False, {}

    def reset(self):
        pass

    def render(self, mode='human', close=False):
        pass
