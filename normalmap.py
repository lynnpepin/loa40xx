# normalmap.py
# purpose of this is to provide utility functions for normal maps
# and a script for generating a normal map 'palette' for painters

import numpy as np

### OLD CODE
# base_angles are the only ones we are interested in
# on one quarter of the unit circle
base_angles = np.array([0, np.pi/12, np.pi/8, np.pi/6])

# now let's repeat by 4 to get all 360
key_angles = np.array([
  base_angles + ii*np.pi/4
  for ii in range(8)
]).flatten()

# from theta and phi angles, we get our normal angle
def get_normal(theta, phi):
  #theta in xy plane,
  #-pi to pi
  #phi from 0 to pi/2
  zz = np.cos(phi)
  rr = np.sin(phi)
  xx = rr*np.cos(theta)
  yy = rr*np.sin(theta)
  return np.array([xx, yy, zz])

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
    


  
