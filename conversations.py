import characters
import messages as m
import random

class Conversation(object):
  """Abstract base class for all conversations in game."""

  def __init__(self, npc, answer=None):
    self.npc = npc
    self.answer = answer

  def outside_theater_day_one(self.npc):
    """Prints and processes conversations outside
    the theater after orientation on Day One."""

    if self.npc = 'Troid':

      npc_speaking = '\n%s:\n\t' % characters.TROID.name

      m.print_messages([
        m.TROID_DESCRIPTION + m.ENTER,
        npc_speaking + m.TROID_HEY_BRO + m.ENTER,
        npc_speaking + m.TROID_CONVO_ONE + m.ENTER])
      
      self.answer = m.print_messages(m.TROID_CONVO_ONE_ANSWERS)

      if self.answer == '1':
        characters.TROID.dispo += 1
        m.print_messages(npc_speaking + m.TROID_LOVES_X + m.ENTER)        
