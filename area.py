from simpy.events import AnyOf, AllOf, Event

class Area:
  def __init__(self, index, name, population, env):
    self.env = env

    self.index = index
    self.name = name
    self.population = population

    self.moved_out_evt = env.event()
    self.moved_in_evt = env.event()

  def move_in(self):
    while True:
      print "Listening for move_in event on %s" %self.name
      yield self.moved_in_evt
      self.population += 1
      print "%s new population = %d" %(self.name, self.population)

  def move_out(self):
    while True:
      print "Listening for move_out event on %s" %self.name
      yield self.moved_out_evt
      self.population -= 1
      print "%s new population = %d" %(self.name, self.population)

  @staticmethod
  def distance(area1, area2):
      # calculate euclidean distance between points
      return math.sqrt( (area1.x - area2.x)**2 + (area1.y + area2.y)**2 )
