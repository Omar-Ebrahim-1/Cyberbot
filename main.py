import cyberbot as cb
import helpers as h

BOT_SPEED = 100/7
BOT_ROTATION_SPEED = 1/2.5
bot = h.Bot(BOT_SPEED, BOT_ROTATION_SPEED)

initial_sleep = 5000
steps = 6
forward_distance = [30, 75, 10, 70, 10, 30]
turn_degree = 90

cb.sleep(initial_sleep)
for step in range(steps):
  bot.move('f', forward_distance[step])
  if step % 2 == 0:
    bot.turn('l', [turn_degree])
  else:
    bot.turn('r', [turn_degree])
bot.stop()
