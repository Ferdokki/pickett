import Character

from unittest import TestCase

class test_Character(TestCase):
  def test_simple(self):
    character = Character.NonPlayerCharacter(name='test')
    self.assertEqual(str(character),
                     'Name = test, Character Class = NonPlayerCharacter, '
                     'Status: None, Gender: m, Properties: {}')

