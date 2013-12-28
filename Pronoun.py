from collections import namedtuple

Pronoun = namedtuple('Pronoun', 'subject object possessive')

PRONOUN = {
  'm': Pronoun(subject='he', object='him', possessive='his'),
  'f': Pronoun(subject='she', object='her', possessive='her'),
  }
