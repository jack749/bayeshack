import simpy
from actor import Actor

# Simulate on montly basis
def example(env):
  while True:
    print(env.active_process)
    value = yield env.timeout(1, value=42)
    print('now=%d, value=%d' % (env.now, value))

actor = Actor()

print actor

env = simpy.Environment()
p = env.process(example(env))
env.run(until=40)

# until = 10
# while env.peek() < until:
#   env.step()
# env.step()
