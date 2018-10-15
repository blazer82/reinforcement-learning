import gym
import numpy
import uuid
from gym import error, spaces, utils
from gym.utils import seeding
from pypokerengine.api.emulator import Emulator
from pypokerengine.engine.card import Card

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

        self.max_round = 10
        self.initial_stack = 200
        self.small_blind_amount = 5

        self.gym_player_uuid = uuid.uuid4()
        self.gym_player_pos = 1

        self.game_started = False

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
        
        if self.game_started is False:
            self.game_started = True
            self.game_state, events = self.emulator.start_new_round(self.game_state)
            print(self.game_state)
            return self._get_observation(self.game_state), 0.0, False, {}

        return self._get_observation(self.game_state), 0.0, False, {}

    def reset(self):
        self.emulator = Emulator()
        self.emulator.set_game_rule(player_num=2, max_round=self.max_round, small_blind_amount=self.small_blind_amount, ante_amount=0)
        
        self.game_state = self.emulator.generate_initial_game_state(
            {
                uuid.uuid4(): { "name": "random_player", "stack": self.initial_stack },
                self.gym_player_uuid: { "name": "gym_player", "stack": self.initial_stack }
            }
        )

    def render(self, mode='human', close=False):
        pass

    def _get_observation(self, game_state):
        observation = numpy.zeros((32,), dtype=numpy.float32)
        
        # Game
        observation[0] = game_state["table"].seats.size() / 4.
        observation[1] = game_state["table"].seats.count_active_players() / game_state["table"].seats.size()
        observation[2] = float(self.gym_player_pos) / game_state["table"].seats.size()
        observation[3] = float(game_state["table"].sb_pos()) / game_state["table"].seats.size()
        observation[4] = float(game_state["table"].bb_pos()) / game_state["table"].seats.size()

        # Player cards
        i = 5
        for c, card in enumerate(self.game_state["table"].seats.players[self.gym_player_pos].hole_card):
            observation[i + c * 5 + 0] = 1. if card.suit == Card.CLUB else 0.
            observation[i + c * 5 + 1] = 1. if card.suit == Card.DIAMOND else 0.
            observation[i + c * 5 + 2] = 1. if card.suit == Card.HEART else 0.
            observation[i + c * 5 + 3] = 1. if card.suit == Card.SPADE else 0.
            observation[i + c * 5 + 4] = card.rank / 14.

        # Table
        i = 15
        for c, card in enumerate(self.game_state["table"].get_community_card()):
            observation[i + c * 5 + 0] = 1. if card.suit == Card.CLUB else 0.
            observation[i + c * 5 + 1] = 1. if card.suit == Card.DIAMOND else 0.
            observation[i + c * 5 + 2] = 1. if card.suit == Card.HEART else 0.
            observation[i + c * 5 + 3] = 1. if card.suit == Card.SPADE else 0.
            observation[i + c * 5 + 4] = card.rank / 14.

        return observation



