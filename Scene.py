import characters
import messages

from GameState import GAME_STATE

_PAUSE = '$!$!$?!'
_PROMPT = '@#@#@$?!'

def _split_strip(x, sep):
  return [s.strip() for s in x.split(sep)]

def run_scene(scene, *chars, **kwds):
  chars = [characters.find(c) for c in chars]
  sc = scene.format(
    player=GAME_STATE.player,
    character=chars if len(chars) != 1 else chars[0],
    pause=_PAUSE,
    prompt=_PROMPT,
    **kwds)

  prompt = _split_strip(sc, _PROMPT)
  if len(prompt) > 2:
    raise Exception('You can only have one {prompt} in a Scene.')
  if len(prompt) == 2:
    if prompt[1]:
      raise Exception('You can\'t have any text after a prompt')
    has_prompt = True
  else:
    has_prompt = False

  parts = _split_strip(prompt[0], _PAUSE)
  if has_prompt:
    prompt = parts.pop()
  for p in parts:
    raw_input(p + messages.ENTER)
  if has_prompt:
    return raw_input(prompt)
