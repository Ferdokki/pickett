import random

import Messages
import Pronoun
from Properties import Properties

class AbstractCharacter(object):
  """Abstract base class for all characters in the game."""
  _DESCRIPTION_STRING = (
    'Name = {0.name}, '
    'Character Class = {1}, '
    'Status: {0.status}, '
    'Gender: {0.gender}, '
    'Disposition: {0.dispo} '
    'Properties: {0.properties}'
    )

  _CHARACTERS = set()

  def __init__(self, name, dead=False, status=None, gender='m', **properties):
    self.properties = Properties(properties)
    self.name = name
    self.dispo = dispo
    self.dead = dead
    self.status = status  # TODO: shouldn't "dead" be a status?
    self.gender = gender
    self.pronoun = Pronoun.PRONOUN[self.gender]

    self._CHARACTERS.add(self)

  def __str__(self):
    return self._DESCRIPTION_STRING.format(self, self.__class__.__name__)

  def __repr__(self):
    return '%s(%s)' % (self.__class__.__name__, str(self))


class Player(AbstractCharacter):
  pass

class NonPlayerCharacter(AbstractCharacter):
  pass

class Camper(AbstractCharacter):
  def __init__(self, name, camper_in_party=False, **kwds):
    super(Camper, self).__init__(name, **kwds)
    self.camper_in_party = camper_in_party

# TODO: shouldn't we be "rolling" for the stats for the current player?
Player('Pickett', max_hit_points=10, hit_points=10,
       dull=3, innovative=3, homesick=5, arrogant=1, hopeless=3,
       passionate=1, angry=2, paranoid=5, apathetic=4, hyperactive=2,
       )
# There's no need to set these properties to 0 - properties start at 0
# by default.

       # arts_and_crafts=0, animal_handling=0, archery=0, baseball=0,  #start of skills
       # card_games=0, cpr=0, dodgeball=0, empathy=0, first_aid=0,
       # fishing=0, foraging=0, firebuilding=0, intuition=0, knots=0,
       # lacrosse=0, lying=0, music=0, navigation=0, originality=0,
       # pk_rockin=0, presentation=0, rock_climbing=0, sailing=0,
       # stand_up_comedy=0, swimming=0, swag=0, taste=0, theater=0,
       # telekenisis=0, telepathy=0)

NonPlayerCharacter('Angles Gator')
NonPlayerCharacter('Barry Fandling')
NonPlayerCharacter('Barret Falster')
NonPlayerCharacter('Playton Williams')
NonPlayerCharacter('Sherry Fandling', gender='f')
NonPlayerCharacter('Troid')

Camper('Brent Drago')
Camper('Botany Lynn', gender='f')
Camper('Bnola Rae', gender='f')
Camper('Boris Tortavich')
Camper('Can Tabber')
Camper('Freetus Jaunders')
Camper('Gloobin Marfo')
Camper('Gelliot Yabelor')
Camper('Illetia Dorfson', gender='f')
Camper('Kinser Talebearing')
Camper('Nugget Beano')
Camper('Niche Kaguya', gender='f')
Camper('Ninar Tetris', gender='f')
Camper('Pooder Bennet')
Camper('Randy Buffet')
Camper('Trinda Noober', gender='f')
Camper('Trinoba Vyder', gender='')
Camper('Volga Toober', gender='f')
Camper('Yeldstat Krong', gender='f')

def find(name):
  if isinstance(name, Character):
    return name
  lname = name.lower()
  chars = [c for c in Character.CHARACTERS if c.name.lower().startswith(lname)]
  if not chars:
    raise Exception('Can\'t understand character name %s' % name)
  if len(chars) > 1:
    raise Exception('Character name %s is ambiguous: might be %s' %
                    (name, ', '.join(c.name for c in chars)))
  return chars[0]

def get_characters(cclass=None, gender=None):
  results = []
  for c in Character.CHARACTERS:
    if (cclass is None or c.cclass == cclass) and (
        gender is None or c.gender == gender):
      results.append(c)
  return results

def random_character(cclass=None, gender=None):
  return random.choice(get_characters(cclass=cclass, gender=gender))

def random_character_sample(count, cclass=None, gender=None):
  return random.sample(get_characters(cclass=cclass, gender=gender), count)

def choice_list(people):
  """Given a list of people (campers or NPCs), returns a choice list with
  numbers and names."""
  choices = ('%d. %s' % (i + 1, p.name) for (i, p) in enumerate(people))
  return '\n\n'.join(choices)

def choose_person(people, message):
  """Choose a specific person from a list of people."""
  message = message + choice_list(people) + Messages.REQUEST_A_NUMBER
  while True:
    choice = raw_input(message)
    try:
      return people[int(choice) - 1]
    except:
      print Messages.BAD_NUMBER_MESSAGE % len(people)
