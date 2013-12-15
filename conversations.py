import characters
import messages
import random

class Conversation(object):
  """Abstract base class for all conversations in game."""

  def __init__(self, npc, scene, answer=None):
    self.npc = npc
    self.answer = answer
  
  def print_conversations(conversations):
    """Print a bunch of conversations."""
    for c in conversations:
      raw_input(m + messages.ENTER)

  TROID_OUTSIDE_THEATER = ('''
Troid:
    Uh, hey. Whats up
""")
