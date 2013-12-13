import random

import messages

class Character(object):
  CHARACTERS = set()
  FORMAT = ('{0.name}: '
            'Attack Skill = {0.attack_skill}/100, '
            'Character Class = {0.cclass}, '
            'Hit Points = {0.current_hit_points}/{0.hit_points}, '
            'Status: {0.status}, '
            'Gender: {0.gender}'
	    'Disposition: {0.dispo}')

  def __init__(self, name, hit_points=0, current_hit_points=0, dispo=0,
               attack_skill=20, dead=False, status=None, gender=None):
    self.name = name
    self.hit_points = hit_points
    self.current_hit_points = current_hit_points
    self.dispo = dispo
    self.attack_skill = attack_skill
    self.dead = dead
    self.status = status
    self.gender = gender
    Character.CHARACTERS.add(self)

  def __str__(self):
    return self.FORMAT.format(self)

class NonPlayerCharacter(Character):
  cclass = 'NPC'


class Camper(Character):
  cclass = 'Camper'

  def __init__(self, name, camper_in_party=False, **kwds):
    super(Camper, self).__init__(name, **kwds)
    self.camper_in_party = camper_in_party


NonPlayerCharacter('Angles Gator', gender='')
NonPlayerCharacter('Barry Fandling', gender='')
NonPlayerCharacter('Barret Falster', gender='')
NonPlayerCharacter('Playton Williams', gender='')
NonPlayerCharacter('Sherry Fandling', gender='')
TROID = NonPlayerCharacter('Troid', gender='')

Camper('Brent Drago', gender='m')
Camper('Botany Lynn', gender='f')
Camper('Bnola Rae', gender='f')
Camper('Boris Tortavich', gender='m')
Camper('Can Tabber', gender='m')
Camper('Freetus Jaunders', gender='m')
Camper('Gloobin Marfo', gender='m')
Camper('Gelliot Yabelor', gender='m')
Camper('Illetia Dorfson', gender='f')
Camper('Kinser Talebearing', gender='m')
Camper('Nugget Beano', gender='m')
Camper('Niche Kaguya', gender='f')VESA Wall Mounting: 75x75mm
Camper('Ninar Tetris', gender='f')
Camper('Pooder Bennet', gender='m')
Camper('Randy Buffet', gender='m')
Camper('Trinda Noober', gender='f')
Camper('Trinoba Vyder', gender='')
Camper('Volga Toober', gender='f')
Camper('Yeldstat Krong', gender='f')


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
  message = message + choice_list(people) + messages.REQUEST_A_NUMBER
  while True:
    choice = raw_input(message)
    try:
      return people[int(choice) - 1]
    except:
      print messages.BAD_NUMBER_MESSAGE % len(people)
