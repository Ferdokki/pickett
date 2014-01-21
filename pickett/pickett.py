# Pickett by Ray Weiss

import Characters
import Messages

from GameState import GAME_STATE

# PSI_FLAG = False  # What's this?
# RUN_FLAG = True  # What's this?
# These aren't yet used and should either go into GameState or become local
# variables.

def welcome_screen():
  global LAST_NAME
  global DAY

  raw_input(Messages.WELCOME)

  name = raw_input(Messages.ASK_LAST_NAME)
  GAME_STATE.player = Characters.Player(name=name)
  bully = Characters.random_character(cclass='Camper', gender='m')

  print 'Your name is Pickett %s' % GAME_STATE.player.name

  Messages.print_messages([
    Messages.EXPLANATION,
    Messages.BUS_LOADING,
    Messages.CRACK,
    Messages.GAME_KID_LOST])

  return week_one(bully)

def week_one(bully):
  if GAME_STATE.day == 1:
    Messages.print_messages(Messages.WEEK_ONE[GAME_STATE.day])
    campers = Characters.random_character_sample(cclass='Camper', count=5)
    troid = Characters.find('Troid')
    people_outside_theater = campers + [troid]

    while GAME_STATE.characters_talked_to < 3:
      GAME_STATE.characters_talked_to += 1
      person = Characters.choose_person(
        people_outside_theater, Messages.LEAVING_THEATER)

      character_talking = person.name

      if person == troid:
        Messages.print_messages([
          Messages.TROID_DESCRIPTION,
          Messages.PERSON_TALKING % character_talking + Messages.TROID_HEY_BRO,
          Messages.PERSON_TALKING % character_talking + Messages.TROID_CONVO_ONE])

        answer = raw_input(Messages.TROID_CONVO_ONE_ANSWERS)

        if answer == '1':
          troid.dispo += 1
          Messages.print_messages([
            Messages.PERSON_TALKING % character_talking + Messages.TROID_LOVES_X])

        elif answer == '2':
          troid.dispo -= 1
          Messages.print_messages([
            Messages.PERSON_TALKING % character_talking + Messages.TROID_WHATEVER_SMELL])

        elif answer == '3':
          troid.dispo -= 1
          Messages.print_messages([
            Messages.PERSON_TALKING % character_talking + Messages.TROID_WOW])

        else:
          answer = raw_input(Messages.TROID_CONVO_ONE_ANSWERS)
