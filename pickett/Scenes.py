import pickett

class Scene(object):
  """Keeps track of scene variables)"""
  def __init__(self, convo_flag=0, characters_talked_to=0):
    self.convo_flag = convo_flag
    self.characters_talked_to = characters_talked_to

