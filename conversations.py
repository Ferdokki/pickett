import characters
import messages as m
import random

class Conversation(object):
  """Abstract base class for all conversations in game."""

  def __init__(self, character, answer=None):
    self.character = character 
    self.answer = answer 
    
  CHARACTER_SPEAKING = self.character

  def outside_theater_day_one(self.character):
    """Prints and processes conversations outside
    the theater after orientation on Day One."""

    if self.character = 'Troid':

      m.print_messages([
        m.TROID_DESCRIPTION,
        npc_speaking + m.TROID_HEY_BRO,
        npc_speaking + m.TROID_CONVO_ONE])
      
      self.answer = raw_input(m.TROID_CONVO_ONE_ANSWERS)

      if self.answer == '1':
        characters.TROID.dispo += 1
        m.print_messages(CHARACTER_SPEAKING + m.TROID_LOVES_X)        
        return
      elif self.answer == '2':
        characters.TROID.dispo -= 1
        m.print_messages(CHARACTER_SPEAKING + m.TROID_WHATEVER_SMELL)
        return
      elif self.answer == '3':
        characaters.TROID.dispo -= 1
        m.print_messages(CHARACTER_SPEAKING + m.TROID_WOW)
        return
      else:
        m.print_messages(m.NOT_VALID_ANSWER)
        return self.answer = raw_input(m.TROID_CONVO_ONE_ANSWERS)
        
