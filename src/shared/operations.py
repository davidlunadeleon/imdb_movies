import numpy

def get_preference_key(preferences):
  product = numpy.prod(preferences)
  preference_key = (product % 5) + 1
  return preference_key