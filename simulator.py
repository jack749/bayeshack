import simpy
import random
from actor import Actor
from area import Area

class Simulator:
  ACTOR_COUNT = 3
  AREA_COUNT = 3

  def __init__(self, env):
    self.env = env
    self.actor_moved = [i for i in range(3)]
    self.areas = [Area(i, "area %d" %i, 100, env) for i in range(3)]

    self.actors = [Actor(i, self.areas[i], env) for i in range(self.ACTOR_COUNT)]

    self.actor_wait_event_procs = [env.process(self.actors[i].process_event()) for i in range(3)]

    # self.actor_procs = env.process(self.trigger_actor_events())
    self.check_actors_procs = env.process(self.check_actors())

    self.area_move_in_procs = [env.process(self.areas[i].move_in()) for i in range(self.AREA_COUNT)]
    self.area_move_out_procs = [env.process(self.areas[i].move_out()) for i in range(self.AREA_COUNT)]

  def trigger_actor_events(self):
    for i in range(3):
      yield self.env.timeout(45)

      actor = self.actors[i]
      evt = actor.get_event()

      print 'trigger_actor_events: actor %d' %(i)

      evt.succeed()
      actor.create_event()

  def check_actors(self):
    while True:
      yield self.env.timeout(3)

      for i in range(3):
        actor = self.actors[i]
        self.__check_actor_relocation(actor)

  def __check_actor_relocation(self, actor):
    old_area = actor.area

    if actor.index == 1:
      thres = 0
    else:
      thres = 3

    if random.randint(0,5) > thres:
      new_area = self.areas[(old_area.index + 1) % 3]
      actor.move(new_area)
      print "Actor %d moved to new area %d!!!" %(actor.index, new_area.index)
    # else:
      # print "Actor %d staying at area %d!!!" %(actor.index, old_area.index)


env = simpy.Environment()
simulator = Simulator(env)

# env.run(until=120)
env.run(until=120)

for i in range(simulator.AREA_COUNT):
  area = simulator.areas[i]
  print '%s population %d' %(area.name, area.population)

