import characters
import messages
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
      npc_speaking = '\n%s:\n\t'
      raw_input(
        'You see the Counselor from the bus. '    
        'He is wearing a backwards multi-colored hat, '
        't-shirt with a soda, shorts, big sneakears, '
        'and a small cigarette hanging from his mouth.'
        + messages.ENTER)

      raw_input(npc_speaking + 'Hey Bro.' + messages.ENTER) % self.npc

      raw_input(npc_speaking + 'Oh man, it\'s hot, no ' 
      'ladies here either, do you like soda?' + messages.ENTER) 
      
      self.answer = raw_input('1: Yes, 2: No, 3:I\'ve never tried soda.'
                      '\n\nSelect a valid choice :> ') 

      if self.answer == '1':
        characters.TROID.dispo += 1
        raw_input('Yeah totally dude. '
                  'I love feeling extreme')
      
                
