#Pickett by Ray Weiss

import attributes
import characters
import inventory
import feelings
import messages
import monsters
import roll

# GLOBALS
PSI_FLAG = False
LAST_NAME = None
RUN_FLAG = True
BULLY = None
DAY = 1
DEAD = False

class GameState(object):
  """Keeps track game state variables"""
  def __init__(self, convo_flag=0, characters_talked_to=0, convo_log=(None)):
    self.convo_flag = convo_flag
    self.characters_talked_to = characters_talked_to
    self.convo_log = convo_log
  
def welcome_screen():
  global LAST_NAME
  global BULLY
  global DAY

  raw_input(messages.WELCOME)

  LAST_NAME = raw_input(messages.LAST_NAME)
  BULLY = characters.random_character(cclass='Camper', gender='m')

  print 'Your name is Pickett %s' % LAST_NAME

  messages.print_messages([
    messages.EXPLANATION,
    messages.BUS_LOADING,
    messages.CRACK,
    messages.GAME_KID_LOST])

  return week_one(DAY)

def week_one(day):
  if day == 1:
    messages.print_messages(messages.WEEK_ONE[day])
    campers = characters.random_character_sample(cclass='Camper', count=5)
    people_outside_theater = campers + [characters.TROID]

    outside_theater_day_one = GameState()

    if outside_theater_day_one.characters_talked_to != 3:
            
      person = characters.choose_person(
        people_outside_theater, messages.LEAVING_THEATER)

      character_talking = person.name 

      if person == characters.TROID:
        outside_theater_day_one.characters_talked_to = +1
        messages.print_messages([
          messages.TROID_DESCRIPTION,
          messages.PERSON_TALKING % character_talking + messages.TROID_HEY_BRO,
          messages.PERSON_TALKING % character_talking + messages.TROID_CONVO_ONE])

        answer = raw_input(messages.TROID_CONVO_ONE_ANSWERS)
