from gym.envs.registration import register

def register_adventure():
    register(
        id='Adventure-v0',
        entry_point='gym.envs.atari:AtariEnv',
        kwargs={'game': 'adventure', 'obs_type': 'image', 'repeat_action_probability': 0.25},
        max_episode_steps=None,
        nondeterministic=True
    )