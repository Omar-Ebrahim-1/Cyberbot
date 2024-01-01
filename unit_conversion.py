_second_per_millisecond = 1000


def distance_to_milliseconds(
  distances: "list[float]",
  speed: "float"
) -> "list[float]":
  '''
  Convert a list of distances to a list of milliseconds
  distance: list of distances to convert
  '''
  return [
    distance * _second_per_millisecond / speed
    for distance in distances
  ]


def degrees_to_milliseconds(
  degrees: "list[float]",
  rotation_speed: "float"
) -> "list[float]":
  '''
  Convert a list of degrees to a list of milliseconds
  degrees: list of degrees to convert
  '''
  return [
    degree / _rps_to_degrees_per_millisecond(rotation_speed)
    for degree in degrees
  ]


def _rps_to_degrees_per_millisecond(
  rps: "float"
) -> "float":
  '''
  Convert a rotation speed in rotations per second to degrees per millisecond
  rps: rotation speed in rotations per second
  '''
  degrees_per_rotation = 360
  return rps * degrees_per_rotation / _second_per_millisecond
