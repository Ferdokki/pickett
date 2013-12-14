import characters
import messages
import random

class Conversation(object):
  """Abstract base class for all conversations in game."""
  def __init__(self, npc, answer=None):
          self.npc = npc
          self.answer = answer
