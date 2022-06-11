import numpy

def get_preference_key(preferences):
  product = numpy.prod(preferences)
  return (product % 5) + 1