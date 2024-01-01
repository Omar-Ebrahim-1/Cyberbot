import cyberbot as cb
import unit_conversion as uc


class Bot:
  '''
  Helper class for controlling the robot
  '''
  def __init__(
    self: "Bot",
    speed: "float",
    rotation_speed: "float"
  ):
    '''
    speed: speed of the robot in centimeters per second
    rotation_speed: speed of the robot's rotation in rotations per second
    '''
    if speed <= 0:
      raise ValueError('speed must be positive')

    if rotation_speed <= 0:
      raise ValueError('rotation_speed must be positive')

    self._speed = speed
    self._rotation_speed = rotation_speed

  def move(
    self: "Bot",
    directions: "list[str] or str",
    distance: "list[float] or float"
  ):
    '''
    Move in a direction for a specified distance

    directions: list of directions to move in
    Valid directions are 'f', 'b' for forward and backward respectively
    You can also use a non-list for a single direction

    distance: list of distance to move in centimeters
    You can also use a non-list for a single distance
    '''
    directions, distance = Bot._validate_input(self, directions, distance)
    servo_speeds: "dict[str, tuple]" = {
      'f': (75, -75),
      'b': (-75, 75),
    }

    milliseconds = uc.distance_to_milliseconds(distance, self._speed)
    for direction, millisecond in zip(directions, milliseconds):
      cb.bot(18).servo_speed(servo_speeds[direction][0])
      cb.bot(19).servo_speed(servo_speeds[direction][1])
      cb.sleep(millisecond)

  def turn(
    self: "Bot",
    directions: "list[str] or str",
    degrees: "list[float] or float"
  ):
    '''
    Turn in a direction for a specified amount of degrees

    directions: list of directions to turn in
    Valid directions are 'l', 'r' for left and right respectively
    You can also use a non-list for a single direction

    degrees: list of degrees to turn in
    You can also use a non-list for a single degree
    '''
    directions, degrees = Bot._validate_input(self, directions, degrees)
    servo_speeds: "dict[str, tuple]" = {
      'l': (-75, -75),
      'r': (75, 75),
    }

    milliseconds = uc.degrees_to_milliseconds(degrees, self._rotation_speed)
    for direction, millisecond in zip(directions, milliseconds):
      cb.bot(18).servo_speed(servo_speeds[direction][0])
      cb.bot(19).servo_speed(servo_speeds[direction][1])
      cb.sleep(millisecond)

  def stop(self: "Bot", sleep_time: "float" = 0.5):
    '''
    Stop the robot

    sleep_time: time to sleep after stopping in seconds
    '''
    cb.bot(18).servo_speed(0)
    cb.bot(19).servo_speed(0)
    cb.sleep(sleep_time * uc._second_per_millisecond)

  def _validate_input(
    self: "Bot",
    directions: "list[str] or str",
    values: "list[float] or float"
  ) -> "tuple[list[str] or str, list[float] or float]":
    '''
    Validate the input for move and turn
    '''
    if type(values) is list and type(directions) is list:
      if len(values) != len(directions):
        raise ValueError('values and directions must be the same length')

    elif type(values) is not list and type(directions) is list:
      values = [values] * len(directions)
      return directions, values

    elif type(values) is not list and type(directions) is not list:
      values = [values]
      directions = [directions]
      return directions, values

    elif type(values) is list and type(directions) is not list:
      directions = [directions] * len(values)
      return directions, values

    else:
      raise ValueError(
        'values and directions must be lists or non-lists'
      )
