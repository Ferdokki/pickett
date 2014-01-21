class Properties(dict):
  """A collection of properties stored as a dictionary.

  By default, a property is numeric and can be incremented and decremented.
  """
  def get(self, name, default=0):
    return super(Properties, self).get(name, default)

  def increment(self, name, increment=1):
    """Increments a property by a given amount and returns the new value."""
    prop = self.get(name) + increment
    self[name] = prop
    return prop

  def remove(self, name):
    del self[name]
