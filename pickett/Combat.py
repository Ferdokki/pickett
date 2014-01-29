"""
The following code assumes that all characters have the following methods:

  select_action(friends, enemies)
    Returns an action for a combat.  The action might also contain the
    identity of the enemy (or enemies) that the character is attacking - we call
    these "the opponents".

  initiative(action)
    Returns an initiative value, given a choice of action.

  perform_action(action)
    Actually performs the action requested, potentially changing the state of the
    character and the opponents.

    The result is a list of the characters that have left combat at the end of
    this action.  This might include some of the opponents (who have died) or
    the character (who has either died by eir own actions or run away).
"""

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

  actionsw = actions(white, black)
  actionsb = actions(white, black)
  initiatives = initiative(actionsw) + initiative(actionsb)

  for (init, action, char) in sorted(initiatives):
    for leaving in  char.perform_action(action):
      if leaving in white:
        white.remove(leaving)
      else:
        black.remove(leaving)


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
