class player(object):
  def __init__(self):
    self._table = None

class table(object):
  def __init__(self):
    self._players = []

class game(object):
  def __init__(self):
    self._table = table()
    self._players = [player() for x in range(10)]

    for p in self._players:
      p._table = self._table

    self._table._players = self._players