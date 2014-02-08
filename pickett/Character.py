import functools
import random

import Pronoun

from Properties import Properties

D100 = 100
DEFAULT_ATTACK_SKILL = 50
DEFAULT_ATTACK_DAMAGE = 6

# DEFEND has the highest initiative, UNPREPARED the lowest.
UNPREPARED, RETREAT, ATTACK, DEFEND = 0, 1, 2, 3

class Character(object):
  """ base class for all characters in the game."""
  _DESCRIPTION_STRING = (
    'Name = {0.name}, '
    'Character Class = {1}, '
    'Status: {0.status}, '
    'Gender: {0.gender}, '
    'Properties: {0.properties}'
    )

  CHARACTERS = set()

  attack_succeeded_message = '{0.name} hit {1.name} for {damage} points.'
  attack_missed_message = '{0.name} attacked {1.name} - and missed!'
  opponent_died_message = '{0.name} killed {1.name}!'
  retreated_message = '{0.name} retreated...'
  defended_message = '{0.name} defended against attack!'

  def __init__(self, name, dead=False, status=None, gender='m', **properties):
    self.properties = Properties(properties)
    self.name = name
    self.dead = dead
    self.status = status  # TODO: shouldn't "dead" be a status?
    self.gender = gender
    self.pronoun = Pronoun.PRONOUN[self.gender]

    self.CHARACTERS.add(self)

  def prepare_for_turn(self):
    self.combat = UNPREPARED

  def select_action(self, friends, enemies):
    hp = self.properties.get('hit_points')
    if hp < self.properties('retreat_hit_points'):
      return self.retreat
    if hp < self.properties('defend_hit_points'):
      return self.defend
    return functools.partial(self.attack, random.choose(enemies))

  def initiative(self, action):
    return self.properties.get('initiative'), self.combat

  def clean_up_after_turn(self):
    return self.combat == Character.RETREAT

  def attack(self, opponent, messages):
    def messsage(msg, **kwds):
      messages.append(msg.format(self, opponent, **kwds))

    skill = self.properties.get('attack_skill', DEFAULT_ATTACK_SKILL)
    if skill >= random.randrange(D100):
      # Hit!
      max_damage = self.properties.get('attack_damage', DEFAULT_ATTACK_DAMAGE)
      damage = random.randint(1, max_damage)
      points_left = opponent.properties.increment('hit_points', -damage)
      message(self.attack_succeeded_message, damage=damage)
      if points_left <= 0:
        # Your opponent died.
        message(self.opponent_died_message)
        return [opponent]
    else:
      message(self.attack_missed_message)

  def retreat(self, messages):
    self.combat = RETREAT
    messages.append(self.retreated_message.format(self))

  def defend(self, messages):
    self.combat = DEFEND
    messages.append(self.defended_message.format(self))

  def __str__(self):
    return self._DESCRIPTION_STRING.format(self, self.__class__.__name__)

  def __repr__(self):
    return '%s(%s)' % (self.__class__.__name__, str(self))

class Player(Character):
  select_action_message = '(A)ttack, (D)efend, (R)etreat? '
  select_opponent_message = 'Select an opponent (1-%d)'
  dont_understand_action_message = 'I didn\'t understand your action!'

  def select_action(self, friends, enemies):
    while True:
      result = raw_input(self.select_action_message.format(**self)).strip().lower()
      if result:
        if 'defend'.startswith(result):
          return self.defend
        if 'retreat'.startswith(result):
          return self.retreat
        if 'attack'.startswith(result):
          from CharacterDB import choose_person
          enemy = choose_person(
            enemies, self.select_opponent_message.format(**self))
          return functools.partial(self.attack, enemy)
        print(dont_understand_action_message.format(**self))


class NonPlayerCharacter(Character):
  pass

class Camper(Character):
  def __init__(self, name, camper_in_party=False, **kwds):
    super(Camper, self).__init__(name, **kwds)
    self.camper_in_party = camper_in_party
