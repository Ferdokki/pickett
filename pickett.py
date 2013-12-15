#Pickett by Ray Weiss

import attributes
import characters
import inventory
import feelings
import messages
import monsters
import roll
import skills

# GLOBALS
PSI_FLAG = False
LAST_NAME = None
RUN_FLAG = True
BULLY = None
DAY = 1

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
  messages.print_messages(messages.WEEK_ONE[day])
  campers = characters.random_character_sample(cclass='Camper', count=5)
  people_outside_theater = campers + [characters.TROID]
  
  times_talked_outsidetheater = 0
  while times_talked_outside_theater != 3:
    person = characters.choose_person(
      people_outside_theater, messages.LEAVING_THEATER)
  
    print 'You selected %s.' % person
