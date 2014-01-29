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

  CHARACTERS = set()

  def __init__(self, name, dead=False, status=None, gender='m', **properties):
    self.properties = Properties(properties)
    self.name = name
    self.dispo = dispo
    self.dead = dead
    self.status = status  # TODO: shouldn't "dead" be a status?
    self.gender = gender
    self.pronoun = Pronoun.PRONOUN[self.gender]

    self.CHARACTERS.add(self)

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
