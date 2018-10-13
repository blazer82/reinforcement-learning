from gym.envs.registration import register

register(
    id='PyPoker-v0',
    entry_point='gym_pypoker.envs:PyPokerEnv',
    max_episode_steps=None,
    nondeterministic=True
)