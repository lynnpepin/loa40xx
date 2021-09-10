# normalmap.py
# purpose of this is to provide utility functions for normal maps
# and a script for generating a normal map 'palette' for painters

import numpy as np

# Constants
PI = np.pi  # convenience
# All angles for every 15 degrees (pi/12) and every 22.5 degrees (pi/8).
# Union1D makes sure we don't duplicate any angles
key_angles = np.union1d(
    np.arange(0, 2*PI, PI/12),
    np.arange(0, 2*PI, PI/8)
)


def normal_from_angles(theta, phi):
    '''Get a unit vector in R3 described by theta and phi,
    where theta is in the xy plane, (range -pi to pi)
    and phi is the angle from surface to z (range 0 to pi/2)

    :param theta:
    :type theta:
    :param phi:
    :type phi:

    :returns:
    :rtype:
    '''
    #theta in xy plane,
    #-pi to pi
    #phi from 0 to pi/2

    # zz is our 
    zz = np.cos(phi)
    rr = np.sin(phi)
    xx = rr*np.cos(theta)
    yy = rr*np.sin(theta)
    return np.array([xx, yy, zz])

def _test_normal_from_angles():
  # This should return without an AssertionError
  # And it does :)
  for theta in key_angles:
    for phi in key_angles:
      vec = normal_from_angles(theta, phi)
      magnitude = np.linalg.norm(vec)
      assert (magnitude - 1.0) < 0.000001, f"Oh no! Angle {vec} has magnitude {magnitude}"

'''
# now we convert a normal vector to rgb
def normal2rgb(nn):
  return ((nn + 1)*(255/2)).round().astype(np.int)

# this function converts rgb values to hex str
rgb2hex = lambda r,g,b: '#%02x%02x%02x' %(r,g,b)

# and now the script
for phi in key_angles:
  print(f"phi: {(phi*180/np.pi).round()}")
  for theta in key_angles:
    print(rgb2hex(*normal2rgb(get_normal(theta, phi))))

    #`print(f"theta: {(phi*np.pi/180).round()}")`
'''
