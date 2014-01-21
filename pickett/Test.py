from GameState import GAME_STATE

import characters
import Scene

TEST_SCENE_PROMPT = """
{player.name} says hello.
{pause}
{character.name} says go away.
{pause}
Select some crap.
{prompt}
"""

TEST_SCENE_NO_PROMPT = """
{player.name} says hello, {player.pronoun.subject}
{pause}
{wombat}
{character[0].name} says go away.
{pause}
{character[1].name} says "yeah, go away."
"""

def test_scene():
  GAME_STATE.player = characters.Player(name='Testy', gender='f')
  Scene.run_scene(TEST_SCENE_PROMPT, 'troid')
  Scene.run_scene(TEST_SCENE_NO_PROMPT, 'gelliot', 'ille', wombat='I am a wombat')
