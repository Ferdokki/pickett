class GameState(object):
  """Keeps track of game state variables."""
  def __init__(self, convo_flag=0, characters_talked_to=0, already_talked_to=[], 
               convo_log=None, name=None):
    self.convo_flag = convo_flag
    self.characters_talked_to = characters_talked_to
    self.convo_log = convo_log
    self.name = name
    self.dead = False
    self.day = 1
    self.player = None

GAME_STATE = GameState()
