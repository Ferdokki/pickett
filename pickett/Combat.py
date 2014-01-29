import itertools
import operator
import random

"""
The following code assumes that all characters have the following methods:

  prepare_for_turn()
    Prepares a chararacter for the next combat turn.

  select_action(friends, enemies)
    Returns an action for a combat.  The action might also contain the
    identity of the enemy (or enemies) that the character is attacking - we call
    these "the opponents".

    Executing an action return as a list of the characters that have left combat
    at the end of this action.  This might include some of the opponents (who
    have died) or the character (who has either died by eir own actions or run
    away).

  initiative(action)
    Returns an initiative value, given a choice of action.

  clean_up_after_turn()
    Cleans up after a combat turn.  Returns true if this character should leave
    the attack.

"""

def sorted_initiatives(initiatives):
  """Sort players with initiatives.  This would be trivial except that we need
  to randomize initialitives that are the same - we can't rely on the sort not
  to break the game balance - and we also need to reverse the list at the end,
  because we want the highest initiatives to go first!"""
  initialitives = initialitives.sort()
  grouped = itertools.groupby(initialitives, operator.itemgetter(0))
  return reversed(itertools.chain(random.shuffle(list(g)) for g in grouped))

def one_turn(white, black):
  """Perform one turn of combat between two groups of players, named white and
  black."""

  def actions(us, them):
    "Returns a list of (character, action) for each character of us."
    return [char, char.select_action(us, them) for char in us]

  def initiative(char_actions):
    """Returns a list of (initiative, character, action), given a list of
    (character, action) pairs."""
    return [(char.initiative(action), char, act) for char, act in char_actions]

  def remove(character):
    if character in white:
      white.remove(character)
    else:
      black.remove(character)

  for char in white + black:
    char.prepare_for_turn()

  actionsw = actions(white, black)
  actionsb = actions(white, black)
  initiatives = initiative(actionsw) + initiative(actionsb)

  for (init, action, char) in sorted_initiatives(initiatives):
    for leaving in action() or []:
      remove(leaving)

  for character in white + black:
    if character.clean_up_after_turn():
      remove(character)

def combat(white, black):
  # Run turns whilte there are opponents on both sides.
  while white and black:
    one_turn(white, black)

def weapon_attack(attacker, weapon, victim):
  # Some attacks might take a weapon and here's a simple framework
  # for that.
  result = weapon.attack(attacker, victim)
  if result:
    result.apply(attacker, victim)
