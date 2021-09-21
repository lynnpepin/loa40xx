# normalmap.py
# this will be used to generate a palette for hand-painting normals

import numpy as np

# Constants
PI = np.pi
EPS = 0.00000001

# All angles for every 15 degrees (pi/12) and every 22.5 degrees (pi/8).
# Union1D makes sure we don't duplicate any angles
KEY_ANGLES = np.union1d(
    np.arange(0, 2*PI + EPS, PI/12),
    np.arange(0, 2*PI + EPS, PI/8)
)


def normal_from_angles(theta, phi):
    '''Get a unit vector in R3 described by theta and phi,
    where theta is in the xy plane, (range -pi to pi)
    and phi is the angle from surface to z (range 0 to pi/2)
    
      ^Z
      |   Y
      |  /
      | /
      |/_____X
    
    :param theta: Angle along the XY plane, in radians
    :type theta: float
    :param phi: Angle along the Z axis, in radians
    :type phi: float

    :returns:
    :rtype:
    '''
    #theta in xy plane,
    #-pi to pi
    #phi from 0 to pi/2

    # xx, yy, zz are magnitudes in these said directions
    
    zz = np.cos(phi)
    rr = np.sin(phi)
    xx = rr*np.cos(theta)
    yy = rr*np.sin(theta)
    return np.array([xx, yy, zz])

def _test_normal_from_angles_has_mag_1(angles=KEY_ANGLES):
    # This should return without an AssertionError
    # And it does :)
    for theta in angles:
        for phi in angles:
            vec = normal_from_angles(theta, phi)
            magnitude = np.linalg.norm(vec)
            assert (magnitude - 1.0) < 0.000001, f"Oh no! Angle {vec} has magnitude {magnitude}"


            
def normal2rgb(nn):
    '''
    Convert a normal vector (x,y,z) with ranges (-1,1) (float)
    to a normal vector (x,y,z) with ranges (0, 255) (int)
    :param nn: Numpy array with dtype float64
    :type nn: numpy.array
    
    :returns: Int array to be interpreted as RGB tuple
    :rtype: numpy.array
    '''
    return ((nn + 1)*(255/2)).round().astype(np.int)

def rgb2hex(rr, gg, bb):
    '''Convert an RGB tuple to a hex color code
    
    :param rr: Red component, from 0 to 255
    :type rr: int
    :param gg: Green component, from 0 to 255
    :type gg: int
    :param bb: Blue component, from 0 to 255
    :type bb: int
    
    :returns: Hexcode of color (like #3322aa)
    :rtype: string
    
    example:
    >>> rgb2hex(*[10,30,120])
    '#0a1e78'
    
    '''
    return '#%02x%02x%02x' %(r,g,b)


def generate_normal_palette(thetas=KEY_ANGLES, phis=KEY_ANGLES[:9]):
    '''
    :param thetas: Theta angles to render (should be from 0 to 2pi rad)
    :type thetas: List[float]
    :param phis: Phi angles to render  (should be from 0 to pi/2 rad)
    :type phis: List[float]
    
    :return: Numpy array of int of shape(w,h,3) of the color palette
    :type: numpy.array
    '''
    colors = np.zeros(shape=(len(phis), len(thetas), 3), dtype=np.int)
    
    for ii in range(len(phis)):
        for jj in range(len(thetas)):
            phi = phis[ii]
            theta = thetas[jj]
            normal = normal_from_angles(theta, phi)
            color = normal2rgb(normal)
            colors[ii,jj] = color
    
    return colors

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
