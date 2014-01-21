#Pickett by Ray Weiss

import attributes
import Characters
import inventory
import feelings
import messages
import monsters

from GameState import GAME_STATE

# PSI_FLAG = False  # What's this?
# RUN_FLAG = True  # What's this?
# These aren't yet used and should either go into GameState or become local
# variables.

def welcome_screen():
  global LAST_NAME
  global DAY

  raw_input(messages.WELCOME)

  name = raw_input(messages.ASK_LAST_NAME)
  GAME_STATE.player = Characters.Player(name=name)
  bully = Characters.random_character(cclass='Camper', gender='m')

  print 'Your name is Pickett %s' % GAME_STATE.player.name

  messages.print_messages([
    messages.EXPLANATION,
    messages.BUS_LOADING,
    messages.CRACK,
    messages.GAME_KID_LOST])

  return week_one(bully)

def week_one(bully):
  if GAME_STATE.day == 1:
    messages.print_messages(messages.WEEK_ONE[GAME_STATE.day])
    campers = Characters.random_character_sample(cclass='Camper', count=5)
    troid = Characters.find('Troid')
    people_outside_theater = campers + [troid]

    while GAME_STATE.characters_talked_to != 3:
      person = Characters.choose_person(
        people_outside_theater, messages.LEAVING_THEATER)

      character_talking = person.name

      if person == troid:
        GAME_STATE.characters_talked_to = +1
        messages.print_messages([
          messages.TROID_DESCRIPTION,
          messages.PERSON_TALKING % character_talking + messages.TROID_HEY_BRO,
          messages.PERSON_TALKING % character_talking + messages.TROID_CONVO_ONE])

        answer = raw_input(messages.TROID_CONVO_ONE_ANSWERS)

        if answer == '1':
          troid.dispo += 1
          messages.print_messages([
            messages.PERSON_TALKING % character_talking + messages.TROID_LOVES_X])

        elif answer == '2':
          troid.dispo -= 1
          messages.print_messages([
            messages.PERSON_TALKING % character_talking + messages.TROID_WHATEVER_SMELL])

        elif answer == '3':
          troid.dispo -= 1
          messages.print_messages([
            messages.PERSON_TALKING % character_talking + messages.TROID_WOW])

        else:
          answer = raw_input(messages.TROID_CONVO_ONE_ANSWERS)
